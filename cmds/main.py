# -*- coding:utf-8 -*-
import discord
from discord.ext import commands
pray = """
**      **      🛐🛐
      🛐            🛐
🛐                        🛐
            🛐🛐
            🛐🛐
      🛐   🛐
         🛐🛐
               🛐
            🛐🛐🛐
"""
class Pong(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Pong Loaded")
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"bot.latency= {round(self.bot.latency*1000)}ms")
        return 
    @commands.command(name="🛐",pass_context=True)
    async def place_of_worship(self,ctx):
        await ctx.send(pray)
        return 
    commands.command(name="worship",pass_context=True)(place_of_worship.callback)
    commands.command(name="電神",pass_context=True)(place_of_worship.callback)


async def setup(bot):
    await bot.add_cog(Pong(bot))
    print("Main Setup")