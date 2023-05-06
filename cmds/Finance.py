import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from classes.FinanceMgr import FinanceMgr
from classes.Dollar import Dollar
import json, asyncio, os,datetime

class Finance(Cog_Extension):
    @commands.hybrid_command(name="money",description="Show Money")
    async def show_money(self,ctx,unit:Dollar,who:discord.User=None):
        if(who==None): who=ctx.author
        account=FinanceMgr(who.id)
        await ctx.reply(f"<@{who.id}> 有 {account.money()//unit.value} {unit.name}")
    @commands.hybrid_command(name="give_money",description="Give money to someone")
    async def give_money(self,ctx,who:discord.User,amount:int,unit:Dollar):
        if(ctx.author==who):
            await ctx.reply(f"<@{who.id}> 你不能給自己錢")
            return
        payer=FinanceMgr(ctx.author.id)
        receiver=FinanceMgr(who.id)
        if(amount<=0):
            await ctx.reply(f"<@{ctx.author.id}>\t<@{ctx.author.id}>\t<@{ctx.author.id}>\n這樣不好優\t這樣不好優\t這樣不好優\t")
            return 
        if(amount*unit.value>payer.money()):
            await ctx.reply(f"<@{ctx.author.id}> 你沒有足夠的錢")
            return 
        if payer.minus(amount*unit.value,f"Give money to {who.id}") and receiver.add(amount*unit.value,f"{ctx.author.id} give money"):
            await ctx.reply(f"程恭支付 <@{who.id}> {amount} {unit.name}")
            return
        else:
            await ctx.reply(f"支付失敗")
        return



async def setup(bot):
    await bot.add_cog(Finance(bot))