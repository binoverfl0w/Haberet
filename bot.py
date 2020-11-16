# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='&')
bot.load_extension('cog')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("m'shkatrrut jeten"))
    print(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)