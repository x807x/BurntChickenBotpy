import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
import json
import random, os, asyncio
from BotMgr.keep_alive import keep_alive

intents = discord.Intents.all()

with open('./data/token.json', 'r', encoding= 'utf8') as PrivateFile:
	data = json.load(PrivateFile)
with open('./data/setting.json','r',encoding='utf8') as file2:
    SettingData=json.load(file2)

bot = commands.Bot(command_prefix= SettingData['prefix'], owner_ids= data['Owner'],intents=intents)

async def Cog_load():
	for filename in os.listdir('./cmds'):
		if filename.endswith('.py'):
			print(f"Cog_load{filename[:-3]}")
			await bot.load_extension(f'cmds.{filename[:-3]}')
	for filename in os.listdir("./txts"):
		if(filename.endswith('.py')):
			print(f"Cog_load{filename[:-3]}")
			await bot.load_extension(f"txts.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f">> {bot.user.name} is online <<")
    

async def main():
    await Cog_load()
    try:
        keep_alive()
        await bot.start(data['Token'])
    except:
        print("Bot Restart")
        os.system("kill 1")
        os.system("python ./BotMgr/restarter.py")
asyncio.run(main())
