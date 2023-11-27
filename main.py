import discord, json, os, asyncio, time
from datetime import datetime,timezone,timedelta
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()

with open('./data/strings.json','r',encoding='utf8') as file2:
    strings=json.load(file2)
bot = commands.Bot(command_prefix= strings['prefix'],owner_id=int(os.getenv("Owner")),intents=intents,strip_after_prefix=False)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f">> {bot.user.name} is online <<")
    t=time.localtime(time.time())
    print(f">>現在時間 {datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))}")

async def Cog_load():
	for filename in os.listdir('./cmds'):
		if filename.endswith('.py'):
			print(f"Cog_load {filename[:-3]}")
			await bot.load_extension(f'cmds.{filename[:-3]}')
	"""for filename in os.listdir("./txts"):
		if(filename.endswith('.py')):
			print(f"Cog_load {filename[:-3]}")
			await bot.load_extension(f"txts.{filename[:-3]}")
	"""


async def main():
    await Cog_load()
    await bot.start(os.getenv("Token"))
asyncio.run(main())