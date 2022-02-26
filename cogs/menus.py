import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.ext.pages import Paginator

from utils import *

class Menus(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	@commands.slash_command(guild_ids=[865981652856733707], name="help", description="Don't know where to start? Use the /help command!")
	async def help(self, ctx):
		embed = discord.Embed(colour=discord.Colour.purple())
		embed.set_author(name="Help")
		embed.add_field(name="/find_me_a_resource", value="This command will bring up interactive messages that will help you find you something to start with.", inline=False)
		embed.add_field(name="/quick_search <Resource Type> <Topic>", value="This command will bring you directly to the list of URL.", inline=False)
		await ctx.respond(embed=embed)

	@commands.slash_command(guild_ids=[865981652856733707], name="quick_search", description="Find something to start your learning with.")
	async def quick_search(self,
		ctx,
		type: discord.Option(
			str,
			"type of resource",
			choices=get_resource_types(),
			required=True
		),
		topic
	):
		await ctx.defer()
		resources = get_resources_list(type, topic)
		def get_properties_only(dict):
			return (dict["name"], dict["url"])
		pages = []
		properties_of_resources = list(map(get_properties_only, resources))
		properties_of_resources = [properties_of_resources[i:i+5] for i in range(0, len(properties_of_resources), 5)]
		if resources != []:
			for divided_list in properties_of_resources:
				vertical_list=""
				for properties in divided_list:
					name, URL = properties
					vertical_list += f"[{name}]({URL})\n"
				embed = discord.Embed(colour = discord.Colour.purple())
				embed.set_author(name=f"Let's see, {topic} {type}....")
				embed.add_field(name="Here's what I found!", value=vertical_list)
				pages.append(embed)
			paginator=Paginator(pages=pages, use_default_buttons=True, timeout=30)
			await paginator.respond(ctx.interaction)
		else:
			embed = discord.Embed(colour = discord.Colour.red())
			embed.set_author(name=f"I can't seem to find {topic} {type}.")
			embed.add_field(name="You might want to check your spelling.", value="Why not try /find_me_a_resource?", inline=False)
			await ctx.respond(embed=embed)
		
	@commands.slash_command(guild_ids=[865981652856733707], name="find_me_a_resource", description="Find something to start your learning with.")
	async def find_me_a_resource(self, ctx):
		
		resource_type_list = get_resource_types()
		formats_available = ""
		view=View()
		
		async def button_callback(interaction):
			view.clear_items()
			resource_type = interaction.data['custom_id']
			topic_list = get_topics_from_type(resource_type)
			embed = discord.Embed(colour = discord.Colour.purple())
			embed.set_author(name=f"Hmmm, {resource_type}....")
			embed.add_field(name="And what would you like to learn about?", value="Send a topic (e.g. Python, Java, C++)", inline=False)
			await interaction.response.edit_message(embed=embed, view=view)

			try:
				response = await self.client.wait_for('message', check=lambda message: ctx.author == message.author and message.channel == ctx.channel, timeout=30)
				response = response.content
			except Exception:
				#TODO: error handling for timeout
				return
			
			resources = get_resources_list(resource_type, response)
			def get_properties_only(dict):
				return (dict["name"], dict["url"])
			pages = []
			properties_of_resources = list(map(get_properties_only, resources))
			properties_of_resources = [properties_of_resources[i:i+5] for i in range(0, len(properties_of_resources), 5)]
			if resources != []:
				for divided_list in properties_of_resources:
					vertical_list=""
					for properties in divided_list:
						name, URL = properties
						vertical_list += f"[{name}]({URL})\n"
					embed = discord.Embed(colour = discord.Colour.purple())
					embed.set_author(name=f"Let's see, {response} {resource_type}....")
					embed.add_field(name="Here's what I found!", value=vertical_list)
					pages.append(embed)
				paginator=Paginator(pages=pages, use_default_buttons=True, timeout=30)
				await paginator.respond(interaction)
			else:
				embed = discord.Embed(colour = discord.Colour.red())
				embed.set_author(name=f"I can't seem to find {response} {resource_type}.")
				embed.add_field(name="You might want to check your spelling.", value="Try /find_me_a_resource again.", inline=False)
				await ctx.respond(embed=embed)
			
		for item in resource_type_list:
			locals().__setitem__(
				f"button_{item}",
				Button(
					label=str(item),
					style=discord.ButtonStyle.blurple,
					custom_id=str(item)
				)
			)
			view.add_item(locals()[f"button_{item}"])
			formats_available += f"{str(item)}? "
			locals()[f"button_{item}"].callback = button_callback
		embed = discord.Embed(colour=discord.Colour.purple())
		embed.set_author(name="Alright, let's help you find something!")
		embed.add_field(name="How would you like to learn?",value=formats_available)
		await ctx.respond(embed=embed, view=view)

def setup(client):
	client.add_cog(Menus(client))