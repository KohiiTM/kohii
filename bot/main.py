import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

#intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!') # Confirm the bot is online
    await bot.tree.sync()
    print("Slash commands synced")

@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping_slash_command(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! {latency}ms")

async def load_cogs():
    await bot.load_extension("cogs.auto_responses")
      
# Load the Pomodoro Cog
async def load_cogs():
    await bot.load_extension("cogs.pomodoro")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)
        print("Bot fully synchronized")


asyncio.run(main())