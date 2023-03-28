# -*- coding:utf-8 -*-
import discord
from discord.ext import commands
from bot import BCbot
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
    def __init__(self,bot:BCbot):
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
        print(ctx.guild.id)
        await self.place_of_worship.callback
        print("hi")
    @commands.hybrid_command(name="hi",with_app_command=True,guild=discord.Object(id=1048972316924711003),description="say hello")
    async def ping_command(self, ctx: commands.Context) -> None:
        await ctx.defer()
        await ctx.send(f"Hello! <@{ctx.author.id}> !")


async def setup(bot):
    await bot.add_cog(Pong(bot),guild=discord.Object(id=1020914209795604601))
    #await bot.tree.sync(guild=discord.Object(id=1020914209795604601))
    print("Main Setup")