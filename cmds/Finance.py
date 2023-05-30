import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from classes.FinanceMgr import FinanceMgr
from classes.Dollar import Dollar
import json, asyncio, os,datetime

class Finance(Cog_Extension):
    @commands.hybrid_command(name="money",description="Show Money")
    async def show_money(self,ctx,unit:Dollar,user:discord.User=None):
        if(user==None): user=ctx.author
        account=FinanceMgr(user.id)
        await ctx.reply(f"<@{user.id}> 有 {account.money()//unit.value} {unit.name}")

    @commands.hybrid_command(name="give_money",description="Give money to someone")
    async def give_money(self,ctx,user:discord.User,money:int,unit:Dollar):
        if(ctx.author==user):
            await ctx.reply(f"<@{user.id}> 你不能給自己錢")
            return
        payer=FinanceMgr(ctx.author.id)
        receiver=FinanceMgr(user.id)
        if(money<=0):
            await ctx.reply(f"<@{ctx.author.id}>\t<@{ctx.author.id}>\t<@{ctx.author.id}>\n這樣不好優\t這樣不好優\t這樣不好優\t")
            return 
        if(money*unit.value>payer.money()):
            await ctx.reply(f"<@{ctx.author.id}> 你沒有足夠的錢")
            return 
        if payer.minus(money*unit.value,f"Give money to {user.id}") and receiver.add(money*unit.value,f"{ctx.author.id} give money"):
            await ctx.reply(f"程恭支付 <@{user.id}> {money} {unit.name}")
            return
        else:
            await ctx.reply(f"支付失敗")
        return



async def setup(bot):
    await bot.add_cog(Finance(bot))