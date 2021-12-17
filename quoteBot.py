# quoteBot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def random_line(afile):
    lines = afile.read().splitlines()
    myline = random.choice(lines)
    return myline

def get_response(afile):
    file = open(afile, "r+", encoding="utf8")
    resp = random_line(file)
    file.close()
    return resp

bot = commands.Bot(command_prefix='-')

@bot.command(name = 'oncinema', help = 'Responds with a random quote from On Cinema at the Cinema.')
async def oncinema(ctx):
    response = get_response("oncinema.txt")
    await ctx.send(response)

@bot.command(name = 'tim', help = 'Responds with a random quote from Tim Heidecker.')
async def oncinema(ctx):
    response = get_response("tim.txt")
    await ctx.send(response)

@bot.command(name = 'gregg', help = 'Responds with a random quote from Gregg Turkington.')
async def oncinema(ctx):
    response = get_response("gregg.txt")
    await ctx.send(response)

@bot.command(name = 'inspire', help = 'Responds with a random inspirational movie quote.')
async def oncinema(ctx):
    response = get_response("inspirational.txt")
    await ctx.send(response)

@bot.command(name = 'sadness', help = 'Responds with a random sad movie quote.')
async def oncinema(ctx):
    response = get_response("sad.txt")
    await ctx.send(response)

bot.run(TOKEN)