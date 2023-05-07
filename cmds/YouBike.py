import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from time import perf_counter
from classes.YouBikeSearcher import YouBikeSearcher, YouBikeStation
from classes.City import City
import asyncio
table="""
剩餘YouBike
  | 剩餘空車架
  |   | 版本
  |   | | 站點名稱
"""
searcher=YouBikeSearcher()
station=YouBikeStation()
class YouBike(Cog_Extension):
    @commands.hybrid_command(name="youbike",description="get youbike information")
    async def youbike_name(self,ctx,city:City,name:str):
        await ctx.defer()
        await ctx.reply(await searcher.name_get(city.value,name))
        return 
    
    """ @commands.hybrid_command(name="add-common",description="add common used youbike station to your list")
    async def add_common(ctx,id_name):
        return """



async def setup(bot):
    await bot.add_cog(YouBike(bot))