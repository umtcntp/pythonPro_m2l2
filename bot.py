import discord
from config import token
from discord.ext import commands
import os, random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right) 



@bot.command()
async def ping(ctx):
    """Returns the bot's latency."""
    await ctx.send(f'Pong! 🏓 Gecikme: {round(bot.latency * 1000)}ms')


@bot.command()
async def mem(ctx):
    img_name = random.choice(["mem1.png", "mem2.png", "mem3.png"])
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


    
bot.run(token)