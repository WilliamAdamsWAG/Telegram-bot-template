<a id="readme-top"></a>
[![MIT License][license-shield]][license-url]

# About 

## description

This is universal template for Telegram bot. Basic functions already done, but more features will be ready later

## Build with

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* AIogram
* Loguru
* ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

# Quick start

```sh
git clone https://github.com/WilliamAdamsWAG/Telegram-bot-template
```

## start with Docker

1. Enter a token to DOCKERFILE at line 3
2. In console enter:
```sh
docker build . --tag telegram-bot
```
3. Finally run app: 
```sh
docker run telegram-bot
```

## start without docker

1. Enter a token to src/app.py to var TOKEN
2. Install libraries:
```sh
pip install -r requirements.txt
```
3. Run the application: 
```sh
python main.py
```

# License

Distributed under the MIT License. See `LICENSE.txt` for more information.

# Contact

[![Gmail][gmail-shield]][gmail-url]
[![Telegram][telegram-shield]][telegram-url]

[gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:williamadams.aurora@gmail.com
[telegram-shield]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[telegram-url]: https://t.me/WilliamAdams_group
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt