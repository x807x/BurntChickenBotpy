import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
import json
import random, os, asyncio

intents = discord.Intents.all()

with open('./data/token.json', 'r', encoding= 'utf8') as PrivateFile:
	data = json.load(PrivateFile)
with open('./data/setting.json','r',encoding='utf8') as file2:
    SettingData=json.load(file2)

bot = commands.Bot(command_prefix= SettingData['prefix'], owner_ids= data['Owner'],intents=intents)

@bot.event
async def on_ready():
	print(f">> {bot.user.name} is online <<")

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f'cmds.{filename[:-3]}')
for filename in os.listdir("./txts"):
    if(filename.endswith('.py')):
        bot.load_extension(f"txts.{filename[:-3]}")

if __name__ == "__main__":
	bot.run(data['Token'])
