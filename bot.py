import discord, json, os, asyncio, time
from datetime import datetime,timezone,timedelta
from discord.ext import commands
from BotMgr.keep_alive import keep_alive

intents = discord.Intents.all()

with open('./data/token.json', 'r', encoding= 'utf8') as PrivateFile:
	data = json.load(PrivateFile)
with open('./data/setting.json','r',encoding='utf8') as file2:
    SettingData=json.load(file2)

class BCbot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix= SettingData['prefix'],owner_ids= data['Owner'],intents=intents,strip_after_prefix=False)
    
    async def setup_hook(self):
        for filename in os.listdir('./cmds'):
            if filename.endswith('.py'):
                print(f"Cog_load{filename[:-3]}")
                await self.load_extension(f'cmds.{filename[:-3]}')
        for filename in os.listdir("./txts"):
            if(filename.endswith('.py')):
                print(f"Cog_load{filename[:-3]}")
                await self.load_extension(f"txts.{filename[:-3]}")
        await self.tree.sync()
    async def on_ready(self):
        print(f">> {self.user.name} is online <<")
        t=time.localtime(time.time())
        print(f">>現在時間 {datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}")

async def main():
    await BCbot().run(data['Token'])
    try:
        keep_alive()
        await BCbot().run(data['Token'])
    except:
        print("Bot Restart")
        os.system("kill 1")
        os.system("python ./BotMgr/restarter.py")


asyncio.run(main())
