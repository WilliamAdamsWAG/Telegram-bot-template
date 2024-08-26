<a id="readme-top"></a>
[![MIT License][license-shield]][license-url]

# À propos 

## description

Il s'agit d'un modèle universel pour un bot Telegram. Les fonctions de base sont déjà faites, mais d'autres fonctions seront prêtes plus tard.

## Construire avec

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* AIogram
* Loguru
* ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

# Démarrage rapide

```sh
git clone https://github.com/WilliamAdamsWAG/Telegram-bot-template
```

## commencer avec Docker

1. Enter a token to `DOCKERFILE` at `line 3` (Entrer un jeton dans `DOCKERFILE`)
2. Dans la console, entrez:
```sh
docker build . --tag telegram-bot
```
3. Enfin, lancer l'application: 
```sh
docker run telegram-bot
```

## démarrer sans docker

1. Entrez un jeton dans `src/app.py` pour var `TOKEN`
2. Installer les librairies:
```sh
pip install -r requirements.txt
```
3. Exécuter l'application: 
```sh
python main.py
```

# Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

# Contact

[![Gmail][gmail-shield]][gmail-url]
[![Telegram][telegram-shield]][telegram-url]

[gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:williamadams.aurora@gmail.com
[telegram-shield]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[telegram-url]: https://t.me/WilliamAdams_group
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/WilliamAdamsWAG/Telegram-bot-template/blob/master/LICENSE