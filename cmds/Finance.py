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
        await ctx.reply(f"<@{who.id}> 有 {account.money()} 奈元")
    @commands.hybrid_command(name="give_money",description="Give money to someone")
    async def give_money(self,ctx,who:discord.User,nanodollar:int):
        if(ctx.author==who):
            await ctx.reply(f"<@{who.id}> 你不能給自己錢")
            return
        payer=FinanceMgr(ctx.author.id)
        receiver=FinanceMgr(who.id)
        if(nanodollar<=0):
            ctx.reply(f"<@{ctx.author.id}> <@{ctx.author.id}> <@{ctx.author.id}>\n這樣不好優\t這樣不好優\t這樣不好優\t")
        if(nanodollar>payer.money()):
            await ctx.reply(f"<@{who.id} 你沒有足夠的錢")
            return 
        if payer.minus(nanodollar,f"Give money to {who.id}") and receiver.add(nanodollar,f"{ctx.author.id} give money"):
            await ctx.reply(f"程恭支付 <@{who.id}> {nanodollar} 奈元")
            return
        else:
            await ctx.reply(f"支付失敗")
        return



async def setup(bot):
    await bot.add_cog(Finance(bot))