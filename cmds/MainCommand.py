# -*- coding:utf-8 -*-
import discord
from discord.ext import commands
import json
with open("./data/strings.json","r",encoding="utf-8") as string_data:
    string=json.load(string_data)
class MainCommand(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        super().__init__()
    @commands.Cog.listener()
    async def on_ready(self):
        print("MainCommand Loaded")
    @commands.hybrid_command(name="ping",pass_context=True,discription="Send My Ping")
    async def ping(self,ctx):
        await ctx.send(f"bot.latency= {round(self.bot.latency*1000)}ms")
        return 
    @commands.hybrid_command(name="膜拜",pass_context=True)
    async def place_of_worship(self,ctx):
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        if(str(ctx.channel.id) in permission["place_of_worship"]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.reply(string["worship"])
        return
    @commands.command(name="🛐",description="You are so Dian")
    async def TooDian(self,ctx):
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        if(str(ctx.channel.id) in permission["place_of_worship"]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.send(string["worship"])
        return
    @commands.hybrid_command(name="hi",with_app_command=True,description="say hello")
    async def ping_command(self, ctx: commands.Context) -> None:
        await ctx.defer()
        await ctx.send(f"Hello! <@{ctx.author.id}> !")

async def setup(bot):
    await bot.add_cog(MainCommand(bot))
    print("Main Setup")