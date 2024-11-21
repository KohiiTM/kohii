import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
from pymongo.mongo_client import MongoClient
import json

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Get credentials
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

# Load MongoDB URI
MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@kohii.763qm.mongodb.net/?retryWrites=true&w=majority&appName=kohii"


mongo_client = MongoClient(MONGO_URI)
db = mongo_client["kohii"]  # database name

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Set up the bot
bot = commands.Bot(command_prefix='/', intents=intents)

# Define the shutdown command
@bot.tree.command(name="shutdown", description="Gracefully shuts down the bot.")
async def shutdown(interaction: discord.Interaction):
    """Shuts down the bot."""
    if interaction.user.id == 696391065317408778:  # Replace with your Discord user ID
        await interaction.response.send_message("Shutting down the bot. Goodbye! 👋", ephemeral=True)
        await bot.close()  # Gracefully close the bot connection
    else:
        await interaction.response.send_message("You do not have permission to shut down the bot.", ephemeral=True)

@bot.event
async def on_ready():
    """Triggered when the bot is ready."""
    print(f'Logged in as {bot.user}!')  # Confirm the bot is online
    try:
        await bot.tree.sync()  # Sync slash commands
        print("Slash commands synced!")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.event
async def on_disconnect():
    """Triggered when the bot disconnects."""
    mongo_client.close()
    print("MongoDB connection closed.")

@bot.tree.command(name="ping", description="Check the bot's latency")
async def ping_slash_command(interaction: discord.Interaction):
    """Simple ping command to check bot latency."""
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Pong! {latency}ms")

# Load the Pomodoro Cog
async def load_cogs():
    """Load all the bot's cogs."""
    try:
        await bot.load_extension("cogs.pomodoro")
        await bot.load_extension("cogs.auto_responses")
        print("Cogs loaded successfully!")
    except Exception as e:
        print(f"Error loading cogs: {e}")

async def main():
    """Run the bot."""
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

# Start the bot
asyncio.run(main())
