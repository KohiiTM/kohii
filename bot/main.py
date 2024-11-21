import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

#intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready(self):
    print(f'Logged in as {bot.user}!') # Confirm the bot is online
    await bot.tree.sync()
    print("Slash commands synced")

async def on_message(self, message):
    if message.author == self.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send(f'yo {message.author.display_name}')




bot.run(TOKEN)
