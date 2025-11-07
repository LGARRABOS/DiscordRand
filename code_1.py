import os
import random

import nextcord
from nextcord.ext import commands

# Récupération du token via la variable d'environnement DISCORD_TOKEN
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "Le token Discord est introuvable. Défini la variable d'environnement "
        "DISCORD_TOKEN avant de lancer le bot."
    )

# Intents pour gérer les permissions de message
intents = nextcord.Intents.default()
intents.message_content = True

# Création du bot avec nextcord
bot = commands.Bot(command_prefix="!", intents=intents)

# Vérification que le bot est bien en ligne
@bot.event
async def on_ready():
    print(f'{bot.user} est connecté !')

# Fonction pour lancer des dés en prenant en compte les valeurs négatives
def roll_dice(rolls, limit):
    return [random.randint(1, abs(limit)) * (-1 if limit < 0 else 1) for _ in range(abs(rolls))]

# Commande slash pour lancer un dé
@bot.slash_command(name="roll", description="Lancer des dés (par ex. 2d6 ou -1d-10)")
async def slash_roll(ctx: nextcord.Interaction, dice: str):
    try:
        # Convertir "dice" en minuscule pour gérer les majuscules
        dice = dice.lower()
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.response.send_message("Format incorrect ! Utilise le format NdX, par exemple 2d6, -1d10 ou 1d-10.")
        return

    # Lancer les dés en utilisant la fonction modifiée
    results = roll_dice(rolls, limit)
    await ctx.response.send_message(f"Résultat pour {dice}: {results} (Total: {sum(results)})")

# Commande préfixée pour lancer un dé avec "!"
@bot.command(name="roll", help="Lance un dé et retourne un résultat aléatoire (par ex. !roll 2d6 ou !roll -1d-10).")
async def prefix_roll(ctx, dice: str):
    try:
        # Convertir "dice" en minuscule pour gérer les majuscules
        dice = dice.lower()
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send("Format incorrect ! Utilise le format NdX, par exemple 2d6, -1d10 ou 1d-10.")
        return

    # Lancer les dés en utilisant la fonction modifiée
    results = roll_dice(rolls, limit)
    await ctx.send(f"Résultat pour {dice}: {results} (Total: {sum(results)})")

# Lancer le bot
bot.run(TOKEN)
