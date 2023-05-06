import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from classes.FinanceMgr import FinanceMgr
import json, asyncio, os,datetime

class Finance(Cog_Extension):
    @commands.hybrid_command(name="money",description="Show Money")
    async def show_money(self,ctx,who:discord.User=None):
        if(who==None): who=ctx.author
        account=FinanceMgr(who.id)
        ctx.reply(f"<@{who.id}> 有 {account.money()} 奈元")



async def setup(bot):
    await bot.add_cog(Finance(bot))