import discord
from discord import app_commands
from discord.ext import commands
class Pong(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping")
    
    @app_commands.command(name="pong",description="Get Bot's ping")
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.send_message(f"Ping")