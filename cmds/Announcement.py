import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
from classes.AnnouncementMgr import *
from classes.Time import Time
import json, asyncio, os,datetime, threading

async def on_announcement_remove(channel:discord.TextChannel|discord.Thread,delete_old_channel:bool,AG:AnnouncementMgr,bot_name:str):
    if(delete_old_channel):
        await channel.delete()
        return
    await channel.set_permissions(channel.guild.default_role,overwrite=None)
    await channel.send(f"<#{channel.id}> 此頻道已被從{bot_name}的公告頻道移除")
    return 

async def on_announcement_add(channel:discord.TextChannel|discord.Thread,send_msg_permission:bool,bot_name:str):
    if(send_msg_permission==False):
        await channel.set_permissions(channel.guild.default_role,send_messages=False)
    await channel.send(f"@everyone 此處已被設為{bot_name}公告頻道")

class Announcement(Cog_Extension):
    @commands.hybrid_command(name="set_announcement_channel",description="Set A Channel To Get Latest Bot Information")
    async def set_announcement_channel(self, ctx,channel:discord.TextChannel|discord.Thread=None,delete_old_channel:bool=False,send_message_permission:bool=False):
        if channel is None:
            channel=ctx.channel
        await ctx.defer()
        #AnnouncementGuild
        AG=AnnouncementMgr(channel.guild.id)
        if(AG.announcement_channel==channel.id):
            await ctx.reply(f"<#{channel.id}> 已經是公告頻道")
            return
        if(type(channel)!=discord.channel.TextChannel): send_message_permission=True
        if(AG.announcement_channel!=0):
            old=ctx.guild.get_channel_or_thread(AG.announcement_channel)
            if(old!=None): await on_announcement_remove(old,delete_old_channel,AG,self.bot.user.name)
        if AG.mv_announcement(channel.id,send_message_permission):
            await on_announcement_add(channel,send_message_permission,self.bot.user.name)
            await ctx.reply(f"變更成功✅為<#{channel.id}>")
        else:
            await ctx.reply("變更失敗")
    
    @commands.hybrid_command(name="new_announcement_channel",description="create a new announcement channel")
    async def create_announcement_channel(self,ctx:commands.Context,name:str,delete_old_channel:bool=False,send_message_permission:bool=False):
        channel=await ctx.guild.create_text_channel(name)
        if(name==None): name=f"{self.bot.user.name}的公告頻道"
        await ctx.defer()
        AG=AnnouncementMgr(channel.guild.id)
        if(type(channel)!=discord.channel.TextChannel): send_message_permission=True
        if(AG.announcement_channel!=0):
            old=ctx.guild.get_channel_or_thread(AG.announcement_channel)
            if(old!=None): await on_announcement_remove(old,delete_old_channel,AG,self.bot.user.name)
        if AG.mv_announcement(channel.id):
            await on_announcement_add(channel,send_message_permission,self.bot.user.name)
            await ctx.reply(f"創建成功✅為<#{channel.id}>")
        else:
            await ctx.reply("創建失敗")
        return 
    
    @commands.hybrid_command(name="send_announcement",description="Send announcement")
    @commands.is_owner()
    async def send_announcement(self,ctx,content:str):
        AS=AnnouncementSend(self.bot)
        now=datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
        await ctx.defer()
        content=f"""
{content}


來自 <@{self.bot.user.id}>
`{Time()}`
        """
        try:
            await AS.send_announcements(content)
            await ctx.reply("成功發送公告")
        except:
            await ctx.reply("公告發送失敗")
    

        
        

async def setup(bot):
    await bot.add_cog(Announcement(bot))