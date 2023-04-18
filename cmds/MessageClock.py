from discord.ext import commands
from classes.MainClass import Cog_Extension
from time import perf_counter
from discord import app_commands
from classes.Day import Day
from time import time_ns
from functions.TimeExt import time_hash
from classes.Options import Guild_or_channel
import json, discord

#TODO check permission

class MessageClock(Cog_Extension):
    @app_commands.command(name="set-clock",description="set a clock to send message")
    async def add(self,ctx,day:Day,hour:int,minute:int=0,second:int=0):
        target=time_hash(hour,minute,second)
        element={
            "time":target,
            "message":ctx.content,
            "channel_id":ctx.channel.id,
            "author":ctx.author.id,
            "command_id":ctx.message.id
        }
        path=f"./data/guild/clock/{ctx.guild.id}.json"
        try:
            with open(path,"r") as clock_data:
                data=json.load(clock_data)
                clock_data.close()
        except FileNotFoundError:
            data={}
            with open(path,"w") as clock_data:
                json.dump(data,clock_data)
                clock_data.close()
            #TODO start keep running func
        try:
            data[f"{target}"].append(element)
        except KeyError:
            data[f"{target}"]=[element]
        with open(path,"w") as clock_data:
            json.dump(data,clock_data)
            clock_data.close()
        await ctx.reply(f"加入成功")
        return 

    @app_commands.command(name="clock-list",description="show all clock")
    async def show_list(self,ctx,show_id:bool):
        w="```\n"
        count=0
        path=f"./data/guild/clock/{ctx.guild.id}.json"
        try:
            with open(path,"r") as clock_data:
                data=json.load(clock_data)
                clock_data.close()
        except FileNotFoundError:
            data={}
        for time_mark in data:
            first_in_time_mark=True
            for msg in time_mark:
                if(ctx.channel.id!=msg["channel_id"]):
                    continue
                count+=1
                if(first_in_time_mark):
                    time_now=msg["time"]
                    w+=f"{time_now}"#TODOimprove time output
                    first_in_time_mark=False
                content=msg["message"]
                if(show_id):
                    message_id=msg["command_id"]
                    w+=f"\t{content}  {message_id}\n"
                else: w+=f"\t{content}\n"
        if(count==0):
            ctx.reply("這個頻道沒有定時訊息")
            return 
        w+=f"```\n找到{count}個定時訊息"
        await ctx.reply(w)
        return 

    @app_commands.command(name="clear-clock",description="clear all clocks")
    async def clear(self,ctx,all:Guild_or_channel):
        path=f"./data/guild/clock/{ctx.guild.id}.json"
        if(all):
            empty={}
            with open(path,"w") as clock_data:
                json.dump(empty,clock_data)
                clock_data.close()
            ctx.reply("以清除伺服器內所有定時訊息")
            return
        with open(path,"r") as clock_data:
            data=json.load(clock_data)
            clock_data.close()
        channel_id=ctx.channel.id
        for time_mark in data:
            i=0
            while i<len(time_mark):
                if(channel_id==time_mark[i]["channel_id"]):
                    del time_mark[i]
                else:
                    i+=1
        with open(path,"w") as clock_data:
            json.dump(data,clock_data)
            clock_data.close()
        ctx.reply("以清除頻道內所有定時訊息")
        return

    @app_commands.command(name="remove-clock",description="remove a set clock")
    async def remove(self,ctx,command_id:int):
        path=f"./data/guild/clock/{ctx.guild.id}.json"
        with open(path,"r") as clock_data:
            data=json.load(clock_data)
            clock_data.close()
        for time_mark in data:
            for i in range(len(time_mark)):
                if(time_mark[i]["command_id"]==command_id):
                    clock_channel=ctx.guild.get_channel(time_mark[i]["channel_id"])
                    if(clock_channel==None):
                        await ctx.reply("錯誤:此頻道不存在")
                        return
                    
                    del time_mark[i]
                    with open(open,"w") as clock_data:
                        json.dump(data,clock_data)
                        clock_data.close()
                    await ctx.reply()
                    return
        return #TODO