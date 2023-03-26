# -*- coding:utf-8 -*-
import discord
from discord.ext import commands
import json
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
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        print(ctx.channel.id)
        if(str(ctx.channel.id) in permission["place_of_worship"]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.send(pray)
        return
    @commands.command(name="worship",pass_context=True)
    async def place_of_worship2(self,ctx):
        print("worship")
        await self.place_of_worship.callback
        print("hi")


async def setup(bot):
    await bot.add_cog(Pong(bot))
    print("Main Setup")