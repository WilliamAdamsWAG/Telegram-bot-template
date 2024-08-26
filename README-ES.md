<a id="readme-top"></a>
[![MIT License][license-shield]][license-url]

# Acerca de 

## descripción

Esta es una plantilla universal para Telegram bot. Funciones básicas ya hechas, pero más características estarán listas más adelante.

## Construir con

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* AIogram
* Loguru
* ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

# Inicio rápido

```sh
git clone https://github.com/WilliamAdamsWAG/Telegram-bot-template
```

## empezar con Docker

1. Introduzca un token para `DOCKERFILE` en la `línea 3`.
2. En la consola, introduzca:
```sh
docker build . --tag telegram-bot
```
3. Por último, ejecute la aplicación: 
```sh
docker run telegram-bot
```

## iniciar sin docker

1. Introduce un token en `src/app.py` para var `TOKEN`.
2. Instalar librerías:
```sh
pip install -r requirements.txt
```
3. Ejecutar la aplicación: 
```sh
python main.py
```

# Licencia

Distribuido bajo la licencia MIT. Véase `LICENSE` para más información.

# Contacto

[![Gmail][gmail-shield]][gmail-url]
[![Telegram][telegram-shield]][telegram-url]

[gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:williamadams.aurora@gmail.com
[telegram-shield]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[telegram-url]: https://t.me/WilliamAdams_group
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/WilliamAdamsWAG/Telegram-bot-template/blob/master/LICENSE