import discord
from discord.ext import commands
from asyncio import sleep

class Pomodoro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Default Pomodoro times
        self.work_time = 25 * 60  # 25 minutes in seconds
        self.short_break_time = 5 * 60  # 5 minutes in seconds
        self.long_break_time = 15 * 60  # 15 minutes in seconds
        self.cycles = 4  # Number of cycles before a long break

    @discord.app_commands.command(name="start_pomodoro", description="Starts a Pomodoro timer.")
    async def start_pomodoro(self, interaction: discord.Interaction):
        """Starts a Pomodoro timer."""
        await interaction.response.send_message(embed=self.create_embed("Pomodoro Timer", "Starting your Pomodoro session!", 0x00FF00))
        
        for cycle in range(self.cycles):
            # Work period
            await self.notify_timer(interaction, "Work Time", self.work_time, "Focus on your tasks!")
            # Short break after each work cycle
            await self.notify_timer(interaction, "Short Break", self.short_break_time, "Take a short break!")

        # Long break after the final cycle
        await self.notify_timer(interaction, "Long Break", self.long_break_time, "Enjoy your long break!")

        await interaction.followup.send(embed=self.create_embed("Pomodoro Timer", "Pomodoro session completed! 🎉", 0x00FF00))

    async def notify_timer(self, interaction, title, duration, description):
        """Handles individual timer notifications."""
        embed = self.create_embed(title, description, 0xFFD700)
        message = await interaction.followup.send(embed=embed, wait=True)

        for remaining in range(duration, 0, -60):  # Countdown in 1-minute intervals
            embed.description = f"{description}\nTime remaining: {remaining // 60} minutes."
            await message.edit(embed=embed)
            await sleep(60)

        embed.description = f"{title} is over! Moving to the next phase."
        embed.color = 0xFF0000
        await message.edit(embed=embed)

    @discord.app_commands.command(name="set_pomodoro", description="Sets custom Pomodoro timings.")
    async def set_pomodoro(self, interaction: discord.Interaction, work: int, short_break: int, long_break: int, cycles: int):
        """Sets custom Pomodoro timings."""
        self.work_time = work * 60
        self.short_break_time = short_break * 60
        self.long_break_time = long_break * 60
        self.cycles = cycles
        await interaction.response.send_message(
            f"Pomodoro times updated: {work} min work, {short_break} min short break, "
            f"{long_break} min long break, {cycles} cycles.",
            ephemeral=True
        )

    def create_embed(self, title, description, color):
        """Creates an embed for the bot messages."""
        embed = discord.Embed(title=title, description=description, color=color)
        embed.set_footer(text="Pomodoro Timer Bot")
        return embed

# Add this cog to your bot
async def setup(bot):
    await bot.add_cog(Pomodoro(bot))
