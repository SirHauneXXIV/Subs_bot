import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

KEY = 'AIzaSyAzkuSlZEanYS2OsMZiVLg08jdYThPnvsg'

bot = commands.Bot(command_prefix = '!') #Prefijo del bot

@bot.command(name = 'suma')
async def sumar(ctx, num1, num2):
    response = int(num1) + int(num2)
    await ctx.send(response)
    
@bot.command(name = 'mult')
async def multiplicar(ctx, num1, num2):
    response = int(num1) * int(num2)
    await ctx.send(response)
    
@bot.command(name = 'subs')
async def subscriptores(ctx, username):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + KEY).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + "{:,d}".format(int(subs)) + " subscriptores"
    await ctx.send(response)
    
bot.run(TOKEN)
