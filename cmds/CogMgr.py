import discord
from discord.ext import commands
from classes.MainClass import Cog_Extension
import json, asyncio, os


class CogMgr(Cog_Extension):
	@commands.hybrid_command(name="load",description="Load Cog")
	@commands.is_owner()
	async def load(self, ctx, extension):
		await self.bot.load_extension(f'cmds.{extension}')
		await ctx.send(f'Loaded {extension} done.')

	@commands.hybrid_command(name="unload",description="Unload Cog")
	@commands.is_owner()
	async def unload(self, ctx, extension):
		'''卸載 Cog'''
		print(f"Unloading cmds.{extension}")
		await self.bot.unload_extension(f'cmds.{extension}')
		await ctx.send(f'Un - Loaded {extension} done.')

	@commands.hybrid_command(name="reload",description="Reload Cog")
	@commands.is_owner()
	async def reload(self, ctx, extension):
		'''重新裝載 Cog'''
		if extension == '*':
			for filename in os.listdir('./cmds'):
				if filename.endswith('.py'):
					await self.bot.reload_extension(f'cmds.{filename[:-3]}')
			await ctx.send(f'Re - Loaded All done.')
		else:
			await self.bot.reload_extension(f'cmds.{extension}')
			await ctx.send(f'Re - Loaded {extension} done.')

	@commands.hybrid_command(name="shutdown",description="Shutdown the bot")
	@commands.is_owner()
	async def shutdown(self, ctx):
		await ctx.send("Shutting down...")
		await asyncio.sleep(1)
		await self.bot.logout()

async def setup(bot):
    await bot.add_cog(CogMgr(bot))