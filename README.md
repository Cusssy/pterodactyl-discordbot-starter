
# Discord bot starter pterodactyl server 

Es un robot simple para iniciar tu servidor que use Pterodactyl desde un boton en un embed

![](https://img001.prntscr.com/file/img001/8GoskxRyT5Sho2KtxWDP6g.png)


## Instalacion y funcionamiento

Pasos a seguir para hacer funcionar todo

### Configurar config.json

```
{
    "bot_token": "El token de tu bot",
    "server_id": "La ID de tu servidor de Pterodactyl",
    "api_key": "La API key de tu servidor de Pterodactyl",
    "server_address": "La dirección de tu servidor Pterodactyl"
}
```

- bot_token: es el token de tu bot de discord para crear tu bot o conseguir su token se hace [aqui](https://discord.com/developers/applications)

- server_id: es la ID de tu servidor que la puedes ver en el URL 

![ID](https://img001.prntscr.com/file/img001/NLbr50rmQYKwSxfR_LIYYA.png)

- api_key: es la apikey que vas a necestiar para que el bot pueda usar la API de tu panel, se solicita en https://mydomain.com/account/api 

- server_address: es la URL que usas para entrar a tu panel


### Instalar requerimentos y ejecutar el bot

El primer paso sera instalar los requerimentos en el requirements.txt

```bash
pip install -r requirements.txt
```

Despues de que todo se haya instalado tenemos que ejecutar el bot
```bash
python3 main.py
```

Yo he ejecutado el bot con [Python 3.9.13](https://www.python.org/downloads/release/python-3913/) no se si funciona en otra version

### Ejecutar en docker

No he podido hacer que funcione en docker :(

ya que he usado funciones que no habia usado nunca antes y hay errores que no se arreglar todavia, en heroku tampoco he podido hacer que me funcione, pero talvez a ti si, si lo conseguies no dudes en contactarme! 

