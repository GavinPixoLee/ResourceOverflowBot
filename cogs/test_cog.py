import discord
from discord.ext import commands

class TestCog(commands.Cog):
	def __init__(self, client):
		self.client = client	

	@commands.slash_command(guild_ids=[865981652856733707], name="help", description="Don't know where to start? Use the /help command!")
	async def help(self, ctx):
		embed = discord.Embed(colour=discord.Colour.purple())
		embed.set_author(name="Help")
		embed.add_field(name="/Find_me_a_resource", value="This command will bring up interactive messages that will help you find your perfect starting point!", inline=False)
		embed.add_field(name="/Where_is <Resource Type> <Topic>", value="This command will bring you directly to the URL of the resource.", inline=True)

		await ctx.respond(embed=embed)

def setup(client):
	client.add_cog(TestCog(client))