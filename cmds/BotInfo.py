import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
import datetime
import json, random
with open("./data/config.json","r",encoding="utf-8") as config_file:
    config=json.load(config_file)

def output(time:float)->str:
    time=int(time*1000)
    if(time>=1000): return f"{time} ms"
    if(time>=100): return f" {time} ms"
    if(time>=10): return f"  {time} ms"
    if(time>=0): return f"   {time} ms"
    return "ERROR"
class BotInfo(Cog_Extension):
    @commands.hybrid_command(name="ping",pass_context=True,description="Send My Ping")
    async def ping(self,ctx:commands.Context):
        now=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=0)))
        a=ctx.message.created_at
        delta=now-a
        msg=await ctx.send(f"```py\nbot_latency  = {output(self.bot.latency)}\nreceive_ping = {output(delta.total_seconds())}```")
        now=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=0)))
        b=msg.created_at
        delta=now-b
        await msg.edit(content=msg.content[:-3]+f"\nsend_ping    = {output(delta.total_seconds())}```")
        return

    @commands.hybrid_command(name="github",description=f"My GitHub Link")
    async def github_link(self,ctx):
        await ctx.reply(config["GithubLink"])
        return 

    """ @commands.hybrid_command("help",pass_context=True,description=config["bot_name"]+" 使用指南")
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
    await bot.add_cog(BotInfo(bot))