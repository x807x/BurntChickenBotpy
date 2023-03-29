# -*- coding:utf-8 -*-
import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
import json
with open("./data/strings.json","r",encoding="utf-8") as string_data:
    strings=json.load(string_data)

class MainCommand(Cog_Extension):
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
        await ctx.reply(strings["worship"])
        return

    @commands.command(name="🛐",description="You are so Dian")
    async def TooDian(self,ctx):
        with open(file="./data/cmd_useable.json",mode="r",encoding="utf-8") as permission_json:
            permission=json.load(permission_json)
        if(str(ctx.channel.id) in permission["place_of_worship"]["unable"]):
            await ctx.reply("You can't use this command in this guild")
            return
        await ctx.send(strings["worship"])
        return

    @commands.hybrid_command(name="hi",with_app_command=True,description="say hello")
    async def ping_command(self, ctx: commands.Context) -> None:
        await ctx.defer()
        await ctx.send(f"Hello! <@{ctx.author.id}> !")

    """ @commands.hybrid_command("help",pass_context=True,discription=strings["bot_name"]+" 使用指南")
    async def help(self,ctx):
        help_string="Commands\n"
        ctx.context
        for cog in self.bot.cogs:
            if cog.lower() == input[0].lower():
                    # making title - getting description from doc-string below class
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                        color=discord.Color.green())
                    # getting commands from cog
                    for command in self.bot.get_cog(cog).get_commands():
                        # if cog is not hidden
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    # found cog - breaking loop
                    break
        return"""

async def setup(bot):
    await bot.add_cog(MainCommand(bot))