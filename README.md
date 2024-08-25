
[![MIT License][license-shield]][license-url]

# Quick start

```sh
git clone https://github.com/WilliamAdamsWAG/Telegram-bot-template`

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
