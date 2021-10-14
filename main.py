import discord
import os
import time
import pymongo
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

mongo = pymongo.MongoClient("mongodb+srv://bean:<password>@beaner.zc5hw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongo.test

client = discord.Client()

client = commands.Bot(command_prefix = '.') #put your own prefix here

@client.event
async def on_ready():
    print(f"Logged into {}".client.u)

def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))


client.run(os.getenv("a")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server

# do you like peanuts
# peanut rated your mother