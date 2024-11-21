import discord
from discord.ext import commands

class AutoResponses(commands.Cog):
    """Cog for handling auto-responses."""

    def __init__(self, bot):
        self.bot = bot  # Correctly assign the bot instance

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return

        # Example 1: Respond to "hello" in chat
        if "valorant" in message.content.lower():
            await message.channel.send("https://tenor.com/view/choso-jjk-choso-choso-panic-insane-choso-anime-insane-gif-5693401929827560865")

        if "hello" in message.content.lower():
            await message.channel.send(f"Yo, {message.author.display_name}!")

        # Example 2: Respond to "how are you?"
        if "how are you" in message.content.lower():
            await message.channel.send("good.")

        # Example 3: Respond to "goodbye"
        if "goodbye" in message.content.lower():
            await message.channel.send("Peace!")

        # Allow command processing to continue
        await self.bot.process_commands(message)

# Setup function to load the cog
async def setup(bot):
    await bot.add_cog(AutoResponses(bot))
