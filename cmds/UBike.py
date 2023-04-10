import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
import json, asyncio, os, ssl, urllib.request

url_tp = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
url_ty="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
url_hc="https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"
url_tc="https://datacenter.taichung.gov.tw/swagger/OpenData/9af00e84-473a-4f3d-99be-b875d8e86256"
context = ssl._create_unverified_context()
def get_ubike(id:int):
    with urllib.request.urlopen(url_tp, context=context) as jsondata:
        data = json.loads(jsondata.read().decode('utf-8')) 
        jsondata.close()
    l=0;r=len(data)
    station=None
    while r-l>=1:
        mid=(l+r)//2
        temp=int(data[mid]["sno"])
        if(temp==id):
            station=data[mid]
            break
        elif(id<temp): r=mid
        else: l=mid
        if(r-l==1 and id!=temp):
            break
    if(station!=None):return station
    with urllib.request.urlopen(url_ty,context=context) as jsondata:
        data=json.loads(jsondata.read().decode('utf-8'))
        jsondata.close()
    data=data["retVal"]
    try: return data[str(id)]
    except KeyError:
        station=None
    with urllib.request.urlopen(url_hc,context=context) as jsondata:
        data=json.loads(jsondata.read().decode('utf-8'))
        jsondata.close()
    for i in data["retVal"]:
        if(id==int(i["sno"])):
            station=i
    if(station!=None): return station
    with urllib.request.urlopen(url_tc,context=context) as jsondata:
        data=json.loads(jsondata.read().decode('utf-8'))
        jsondata.close()
    for i in data["retVal"]:
        if(id==int(i["sno"])):
            station=i
    if(station!=None): return station
    
    
    return None

with open("./data/strings.json","r",encoding="utf-8") as strings_data:
    strings=json.load(strings_data)

class UBike(Cog_Extension):
    class_name="UBike"
    @commands.hybrid_command(name="ubike",description="get ubike information")
    async def ubike(self,ctx,station_id:int):
        station=get_ubike(station_id)
        if(station==None):
            await ctx.sent("Can't find this station")
            return 
        station_name=station["sna"]
        bike=station["sbi"]
        empty=int(station["tot"])-int(station["sbi"])
        await ctx.send(f"{station_name} 剩餘U-Bike {bike}輛 剩餘 {empty}個停車架")
        return


async def setup(bot):
    await bot.add_cog(UBike(bot))