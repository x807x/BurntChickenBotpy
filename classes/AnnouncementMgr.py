import json,time, os
from functions.Writer import *
from discord.ext import commands
import asyncio
import discord
class AnnouncementMgr:
    def __init__(self,GuildID:int):
        self.id=GuildID
        path=f"./data/guild/{self.id}.json"
        try:
            with open(path,"r") as file:
                data=json.load(file)
                file.close()
            data["GuildID"]=self.id
            with open(path,"w") as file:
                json.dump(data, file)
                file.close()
        except FileNotFoundError:
            self.file_repair()
            with open(path,"r") as file:
                data=json.load(file)
                file.close()
            data["GuildID"]=self.id
            with open(path,"w") as file:
                json.dump(data, file)
                file.close()
        except KeyError: self.key_repair("GuildID")
        try:
            self.announcement_channel=data["Announcement"]["ChannelID"]
        except KeyError:
            self.key_repair("Announcement")
        return 

    def key_repair(self,path:str):
        path=path.split("/")
        with open(f"./data/user/{self.id}.json","r") as file:
            data=json.load(file)
            file.close()
        new=json.load(open(f"./data/user/1.json","r"))
        fix(path,data,new)
        with open(f"./data/user/{self.id}.json","w") as file:
            json.dump(data,file)
            file.close()
        return

    def file_repair(self):
        cp("./data/guild/1.json",f"./data/guild/{self.id}.json")

    def mv_announcement(self,channel:int,second=False)->bool:
        path=f"./data/guild/{self.id}.json"
        try:
            with open(path,"r",encoding="utf-8") as file:
                data=json.load(file)
                file.close()
            data["Announcement"]["ChannelID"]=channel
            self.announcement_channel=channel
            with open(path,"w",encoding="utf-8") as file:
                json.dump(data,file)
                file.close()
            return True
        except FileNotFoundError:
            if(second): FileNotFoundError
            self.file_repair()
        except KeyError:
            if(second): KeyError
            self.key_repair("Announcement")
        return self.mv_announcement(channel,second=True)
    
class AnnouncementSend:
    def __init__(self,bot):
        self.bot=bot
        return
    
    def key_repair(self,filename:int,path:str):
        path=path.split("/")
        with open(f"./data/guild/{filename}.json","r") as file:
            data=json.load(file)
            file.close()
        new=json.load(open(f"./data/guild/1.json","r"))
        fix(path,data,new)
        with open(f"./data/guild/{filename}.json","w") as file:
            json.dump(data,file)
            file.close()
        return

    async def send_announcements(self,content):
        tasks=[]
        for filename in os.listdir("./data/guild"):
            if(filename.endswith(".json")==False): continue
            if(filename=="1.json"): continue
            with open(f"./data/guild/{filename}") as file:
                data=json.load(file)
            try:
                temp=data["Announcement"]["ChannelID"]
                if(temp!=0):
                    tasks.append(self.send_announcement(int(filename[:-5]),temp,content))
            except KeyError:
                self.key_repair(filename,"Announcement/ChannelID")
        await asyncio.gather(*tasks)
    
    async def send_announcement(self,GuildID:int,ChannelID:int,content:str):
        guild:discord.Guild=self.bot.get_guild(GuildID)
        channel=guild.get_channel_or_thread(ChannelID)
        await channel.send(content)
