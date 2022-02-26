import discord
from discord.ext import commands
from discord.ui import Button, View


resource_type_list = ["Courses", "Books"]

class TestCog(commands.Cog):
	def __init__(self, client):
		self.client = client	

	@commands.slash_command(guild_ids=[865981652856733707], name="help", description="Don't know where to start? Use the /help command!")
	async def help(self, ctx):
		embed = discord.Embed(colour=discord.Colour.purple())
		embed.set_author(name="Help")
		embed.add_field(name="/Find_me_a_resource", value="This command will bring up interactive messages that will help you find you something to start with.", inline=False)
		embed.add_field(name="/Where_is <Resource Type> <Topic>", value="This command will bring you directly to the URL of the resource.", inline=False)

		await ctx.respond(embed=embed)

	@commands.slash_command(guild_ids=[865981652856733707], name="find_me_a_resource", description="Find something to start your learning with.")
	async def find_me_a_resource(self, ctx):
		formats_available = ""
		view=View()
		for item in resource_type_list:
			view.add_item(Button(label=str(item), style=discord.ButtonStyle.blurple))
			formats_available += f"{str(item)}? "
		embed = discord.Embed(colour=discord.Colour.purple())
		embed.set_author(name="Alright, let's help you find something!")
		embed.add_field(name="How would you like to learn?",value=formats_available)

		await ctx.respond(embed=embed, view=view)

def setup(client):
	client.add_cog(TestCog(client))