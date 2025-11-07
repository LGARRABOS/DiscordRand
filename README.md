# DiscordRand

Bot Discord de lancer de dés basé sur [nextcord](https://github.com/nextcord/nextcord).

## Prérequis

- Python 3.11 ou supérieur pour un lancement local.
- [Docker](https://docs.docker.com/get-docker/) si tu souhaites utiliser le conteneur.
  - Sous Windows et macOS, lance **Docker Desktop** et assure-toi que le démon Docker est démarré avant d'exécuter `docker build`.
  - Tu peux vérifier que Docker est prêt avec `docker info`.

## Configuration

1. Crée un bot dans le [portail développeur de Discord](https://discord.com/developers/applications) et récupère son token.
2. Dans ton environnement d'exécution (local ou Docker), définis la variable d'environnement `DISCORD_TOKEN` avec ce token.

### Exemples pour définir `DISCORD_TOKEN`

- **Linux / macOS / PowerShell**

  ```bash
  export DISCORD_TOKEN="ton_token"
  ```

- **PowerShell (persistant)**

  ```powershell
  [Environment]::SetEnvironmentVariable("DISCORD_TOKEN", "ton_token", "User")
  ```

- **Invite de commandes Windows**

  ```bat
  set DISCORD_TOKEN=ton_token
  ```

## Lancer en local

```bash
pip install -r requirements.txt
python code_1.py
```

Le bot se connecte automatiquement et expose les commandes `!roll` et `/roll`.

## Construire et lancer avec Docker

1. Place-toi à la racine du projet (là où se trouve le `Dockerfile`).
2. Construis l'image en précisant le contexte `.` :

   ```bash
   docker build -t discordrand .
   ```

   > Si tu obtiens l'erreur `The system cannot find the file specified`, vérifie que Docker Desktop est démarré.

3. Lance le conteneur en passant le token :

   ```bash
   docker run --rm -e DISCORD_TOKEN="ton_token" discordrand
   ```

Le conteneur se connectera à Discord en utilisant le token fourni. L'option `--rm` supprime automatiquement le conteneur à l'arrêt.
