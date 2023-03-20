import discord
from discord import app_commands
from discord.ext import commands

class Pong(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping")
    @app_commands.command(name="ping",description="Get Bot's ping")
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.send_message(f"Ping",ephemeral=True)
        return


async def setup(bot):
    await bot.add_cog(Pong(bot),guilds=[discord.Object(id=1065833518871085107)])
    print("Main Setup")