import discord
from discord.ext import commands
import json, datetime
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__cog_name__} Loaded")

class Logger:
    def log(self, ctx, data, type='error'):
        time = datetime.datetime.now().strftime('[%Y-%m-%d] [%H:%M]')
        user = ctx.author.name
        channel = ctx.channel.name
        command = ctx.command
        if type == 'error':
            print(f'🔥<Error Log>: {time}/[{user}][{channel}][{command}]: {data}')