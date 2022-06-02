import sqlite3
import json
import discord
from discord.ext import commands
from discord import Activity
import time
import threading
from manager import Manage
import sv
import asyncio
from regex import P
import requests

##I am logging IP, HWID and computer name into the database. 
## Just for more admin info :)




##Config
config = json.loads(open("config.json","r").read())

##Connections
management = Manage()
bot = commands.Bot(command_prefix=config["prefix"], description=config["description"], help_command=None)


##Discord Bot

@bot.event
async def on_connect():
    print("Connecting to Discord...")

@bot.event
async def on_ready():
    print("Bot is online!")
    await bot.change_presence(activity=Activity(type=3, name="{} | Prefix: {}".format(config["servername"], config["prefix"])))
    threading.Thread(target=(sv.run),).start()
@bot.event 
async def on_disconnect():
    print("Disconnected from Discord...")

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        color=discord.Color.green(),
        title = "Help for {}".format(config["servername"]),
        )
    
    for command in config["commands"]:
        embed.add_field(name="{}{}".format(config["prefix"],command), value=config["commands"][command])
    await ctx.send(embed=embed)

@bot.command()
async def addhwid(ctx, *, hwid):
    ip = "None"
    cname = "None"
    if ctx.message.author.guild_permissions.administrator:
        management.insert(hwid, ip,cname)
        return await ctx.send(embed=discord.Embed(
            color=discord.Color.green(),
            description="{} succesfully added!".format(hwid)
        ))
    else:
        return await ctx.send(embed=discord.Embed(
            color=discord.Color.red(),
            description="You are not an admin!"
        ))

@bot.command()
async def checkuser(ctx, type, arg):
    if str(type).lower() == "ip":t="ip"
    elif str(type).lower()=="hwid": t="hwid"
    elif str(type).lower()=="cname": t="cname"

    info = management.get(type, arg)[0]
    ip = info[1]
    hwid = info[0]
    cname = info[2]
    await ctx.send(embed=discord.Embed(
        color=discord.Color.green(),
        description="HWID: {}\nIP: {}\nComputer Name: {}".format(hwid,ip,cname),
        title="Success!"
    ))

@bot.command()
async def remove(ctx, type=None, arg=None):
    if type == None or arg == None: return await ctx.send(embed=discord.Embed(color=discord.Color.red(), description="Usage: {}remove (type) (argument)".format(config["prefix"])))
    r = management.remove(type,arg)
    await ctx.send(embed=discord.Embed(
        color=discord.Color.green(),
        description="Successfully removed user from database!"
    ))
    return True

bot.run(config["token"])