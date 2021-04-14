import discord
from discord.ext import commands
import os
import colorama
from colorama import Fore
 
token = "YOUR_TOKEN" # Paste your discord token here!
 
prefix = "+" # Customize the prefix.
 
title = '''ran by misspoken (:''' # Input a title here, like, Ran By Misspoken!
 
linky = "https://put.a.random.link.here" # Over here you make a fake link, like https://misspoken.on.top or something anything
 
footer = "Put a footer here lol" # This will be at the end of the image, Example: Misspoken owns you!
 
# Example of command, +embed https://cdn.discordapp.com/attachments/811716182481698847/811729488861724722/Random-FB-BANNER.png
 
client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
 
def Clear():
    os.system('cls')
 
os.system('cls' if os.name == 'nt' else 'clear')
@client.event
async def onready():
    print(f'''{Fore.RED}
 
Pays.Host Alt Self-Bot! Made by Misspoken! (:
 
__{prefix}embed <link>
    ''' + Fore.RESET)
 
 
@client.command()
async def embed(ctx, link):
  await ctx.message.delete()
  embd = discord.Embed(
    title =title,
    description = '',
    colour = discord.Colour.blue()) # You can change the color of the embed here if you want.
  embd.set_footer(text=footer)
  embd.set_image(url=link)
  await ctx.channel.send(linky, embed=embd)
client.run(token, bot=False)
 
client.run(token)