import discord
from discord.ext import commands
from pydactyl import PterodactylClient
import json

with open('config.json') as configfile:
    configdata = json.load(configfile)


def StartServer():
    api = PterodactylClient(configdata["server_address"], configdata["api_key"])
    srv_id = configdata["server_id"]
    api.client.servers.send_power_action(srv_id, 'start')

class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Iniciar servidor", 
        style=discord.ButtonStyle.primary,
        emoji="🔌",
        custom_id="start_button")
    async def button_callback_start(self, button: discord.ui.Button,interaction: discord.Interaction):
        await interaction.response.send_message(content=":yellow_circle: El servidor se está encendiendo", ephemeral=True)
        StartServer()

class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=commands.when_mentioned_or("!"), intents=intents)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(PersistentView())
            self.persistent_views_added = True

        print(f"Loggeado en {self.user} (ID: {self.user.id})")
        print("------")

bot = PersistentViewBot()

@bot.command()
async def create_embed(ctx: commands.Context):
    embed = discord.Embed(
        title="Encender Servidor", 
        description="Pulsa el botón de la parte inferior para encender el servidor.",
        )
    await ctx.send(embed=embed,view=PersistentView())

bot.run(configdata["bot_token"])
