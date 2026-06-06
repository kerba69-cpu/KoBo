import discord
from discord.ext import commands
import json
import os

# Keep-Alive Webserver
from keep_alive import keep_alive

# -----------------------------
# Config laden
# -----------------------------
with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["DISCORD_TOKEN"]
PREFIX = config.get("PREFIX", "!")

# -----------------------------
# Bot Setup
# -----------------------------
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# -----------------------------
# Cogs automatisch laden
# -----------------------------
@bot.event
async def on_ready():
    print(f"KoBo ist online als {bot.user}")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Cog geladen: {filename}")

# -----------------------------
# Keep Alive starten
# -----------------------------
keep_alive()

# -----------------------------
# Bot starten
# -----------------------------
bot.run(TOKEN)
