import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from classes.FinanceMgr import FinanceMgr
import json, asyncio, os,datetime
def get_day():
    a=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
    hash=a.day+32*a.month+400*a.year
    return hash

class Daily(Cog_Extension):
	@commands.hybrid_command(name="daily",description="Daily check")
	async def daily(self, ctx,content:str=""):
		try :
			data=open(f"./data/user/{ctx.author.id}.json","r")
			data=json.load(data)
		except FileNotFoundError:
			with open("./data/user/1.json","r") as file:
				data=json.load(file)
				file.close()
			data["UserID"]=ctx.author.id
			with open(f"./data/user/{ctx.author.id}.json","w") as file:
				json.dump(data,file)
		try:
			day=data["Daily"]["LastCheck"]
			if(day==get_day()):
				await ctx.reply(f"<@{ctx.author.id}> 已經遷到過了")
				return 
			data["Daily"]["LastCheck"]=get_day()
		except KeyError:
			data["Daily"]={}
			data["Daily"]["LastCheck"]=get_day()
		
		with open(f"./data/user/{ctx.author.id}.json","w") as file:
			json.dump(data,file)
		user=FinanceMgr(ctx.author.id)
		user.add(int(1e9+7)*1000000,"Daily check")
		print(f"{ctx.author.name}: daily")
		if(content==""): await ctx.reply(f"<@{ctx.author.id}> 已簽到")
		else: await ctx.reply(f"```\n{content}```||<@{ctx.author.id}> 悄悄留下此訊息||")
		return 

async def setup(bot):
    await bot.add_cog(Daily(bot))