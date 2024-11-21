import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}!')+

intens = discord.Intents.default()
intens.message_content = True

client = Client(intents=intens)
client.run('DISCORD_TOKEN')

