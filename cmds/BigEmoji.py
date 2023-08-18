import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
import json, asyncio, os
with open("./data/strings.json","r",encoding="utf-8") as string_data:
    strings=json.load(string_data)

class BigEmoji(Cog_Extension):
    class_name="BigEmoji"
    @commands.command(name="🛐",description="You are so Dian")
    async def TooDian(self,ctx):
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        if(str(ctx.channel.id) in permission[self.__cog_name__]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.send(strings["🛐"])
        return

    @commands.command(name="⚡",description="You are too Dian")
    async def electric(self,ctx):
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        if(str(ctx.channel.id) in permission[self.__cog_name__]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.send(strings["⚡"])
        return
   
    @commands.command(name="⚡️",description="You are too Dian")
    async def electric(self,ctx):
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        if(str(ctx.channel.id) in permission[self.__cog_name__]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.send(strings["⚡"])
        return


async def setup(bot):
    await bot.add_cog(BigEmoji(bot))