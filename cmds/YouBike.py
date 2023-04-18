import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from time import perf_counter
from functions.YouBike import find


class YouBike(Cog_Extension):
    @commands.hybrid_command(name="youbike",description="get youbike information")
    async def youbike(self,ctx,id_name):
        start=perf_counter()
        await ctx.defer()
        await ctx.reply(await find(id_name))
        return 
    
    """ @commands.hybrid_command(name="add-common",description="add common used youbike station to your list")
    async def add_common(ctx,id_name):
        return """



async def setup(bot):
    await bot.add_cog(YouBike(bot))