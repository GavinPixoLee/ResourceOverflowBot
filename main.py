import os
import discord
from discord.ext import commands
from webserver import start as start_server
start_server()

client = commands.Bot(intents=discord.Intents.all())

def get_cogs():
	return map(
		lambda filename: filename[:-3],
		filter(
			lambda filename: filename.endswith(".py") and filename != "__init__.py",
			os.listdir('./cogs')
		)
	)

@client.event
async def on_ready():
	print("online")

@client.event
async def on_command_error(ctx, error):
	await ctx.send(f"{error}")
	raise error

for cog in get_cogs():
	client.load_extension(f'cogs.{cog}')

client.run(os.getenv("DISCORD_BOT_TOKEN"))