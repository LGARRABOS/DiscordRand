# DiscordRand

Bot Discord de lancer de dés basé sur [nextcord](https://github.com/nextcord/nextcord).

## Configuration

1. Crée un bot dans le [portail développeur de Discord](https://discord.com/developers/applications) et récupère son token.
2. Dans ton environnement d'exécution (local ou Docker), définis la variable d'environnement `DISCORD_TOKEN` avec ce token.

```bash
export DISCORD_TOKEN="ton_token"
```

## Lancer en local

```bash
pip install -r requirements.txt
python code_1.py
```

Le bot se connecte automatiquement et expose les commandes `!roll` et `/roll`.

## Construire et lancer avec Docker

```bash
docker build -t discordrand .
```

Pour exécuter l'image en fournissant le token :

```bash
docker run -e DISCORD_TOKEN="ton_token" discordrand
```

Le conteneur se connectera à Discord en utilisant le token fourni.
