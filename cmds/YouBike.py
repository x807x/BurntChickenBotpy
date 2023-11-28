import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from classes.Time import Time
from classes.YouBikeSearcher import YouBikeSearcher, YouBikeStation
from classes.City import City
import asyncio, json
table="""
剩餘YouBike
  | 剩餘空車架
  |   | 版本
  |   | | 站點名稱
"""
with open("./data/config.json","r",encoding="utf-8") as config_file:
    config=json.load(config_file)

searcher=YouBikeSearcher(limit=50)
station=YouBikeStation()
class YouBike(Cog_Extension):
    @commands.hybrid_command(name="youbike",description="get youbike information")
    async def youbike_name(self,ctx:commands.Context,city:City,name:str):
        msg=await ctx.reply(f"查詢{city.name} `{name}` 的站點中...")
        string=f"查詢{city.name} 包含`{name}` 的結果\n"+await searcher.name_get(city.value,name)+f"\n資料來源https://tdx.transportdata.tw/\n`{Time()}`"
        if(len(string)>=2000): await ctx.reply("超出discord長度限制")
        await msg.edit(content=string)
        return 
    
    @commands.hybrid_command(name="youbike_source")
    async def youbike_source(self,ctx:commands.Context):
        with open("./data/pictures/tdxlogo.png","rb") as pic:
            picture=discord.File(pic)
            await ctx.reply(file=picture,content=f"資料來源:{config['TDXLink']}")
    """ @commands.hybrid_command(name="add-common",description="add common used youbike station to your list")
    async def add_common(ctx,id_name):
        return """



async def setup(bot):
    await bot.add_cog(YouBike(bot))