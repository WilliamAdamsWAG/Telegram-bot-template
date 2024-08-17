<a id="readme-top"></a>
[![MIT License][license-shield]][license-url]

# О проекте 

## Описание

Это универсальный шаблон телеграм бота. Базовые функции уже реализованы, но скоро будет добавленно больше возможностей

## Разработано с помощью

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* AIogram
* Loguru
* ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

# Быстрый старт

```sh
git clone https://github.com/WilliamAdamsWAG/Telegram-bot-template
```

## запуск через Docker

1. Вставьте токен в `DOCKERFILE` в `строку 3`
2. Введите в концоли:
```sh
docker build . --tag telegram-bot
```
3. Запустите контейнер: 
```sh
docker run telegram-bot
```

## Запуск без Docker'a

1. Вставьте токен в `src/app.py` в переменную `TOKEN`
2. Установите библиотеки:
```sh
pip install -r requirements.txt
```
3. Запустите приложение: 
```sh
python main.py
```

# Лицензия

Расспростроняется с MIT лицензией. Просмотрите `LICENSE` для более подробной информации.

# Контакты

[![Gmail][gmail-shield]][gmail-url]
[![Telegram][telegram-shield]][telegram-url]

[gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:williamadams.aurora@gmail.com
[telegram-shield]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[telegram-url]: https://t.me/WilliamAdams_group
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/WilliamAdamsWAG/Telegram-bot-template/blob/master/LICENSE