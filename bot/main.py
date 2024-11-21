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

# Define the shutdown command
@bot.tree.command(name="shutdown", description="Gracefully shuts down the bot.")
async def shutdown(interaction: discord.Interaction):
    """Shuts down the bot."""
    if interaction.user.id == 696391065317408778:  # Ensure only I can shut down the bot
        await interaction.response.send_message("Shutting down the bot. Goodbye! 👋", ephemeral=True)
        await bot.close()  # Gracefully close the bot connection
    else:
        await interaction.response.send_message("You do not have permission to shut down the bot.", ephemeral=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!') # Confirm the bot is online
    await bot.tree.sync()
    print("Slash commands synced")
    
@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print("Slash commands synced!")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping_slash_command(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! {latency}ms")


# Load the Pomodoro Cog
async def load_cogs():
    await bot.load_extension("cogs.pomodoro")
    await bot.load_extension("cogs.auto_responses")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)
        print("Bot fully synchronized")


asyncio.run(main())