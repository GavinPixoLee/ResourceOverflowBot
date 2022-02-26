import discord
from discord.ext import commands

class TestCog(commands.Cog):
	def __init__(self, client):
		self.client = client	

	@commands.slash_command(name="")

def setup(client):
	client.add_cog(TestCog(client))