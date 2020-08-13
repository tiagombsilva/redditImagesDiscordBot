import os
import discord
from data import Website,RedditBot
from db import database
from random import randrange
from config import Config
import re

token = Config.json["discord_token"]
guild = Config.json["discord_guild"]

client = discord.Client()
subreddits = Config.subReddits
db = database()

@client.event
async def on_ready():
    print("Iam Online!")
    await client.change_presence(activity=discord.Game("%help"))

@client.event
async def on_message(message):
    if(message.content == ("%help") and not message.author.bot):
        channel = message.channel
        helpMessage = ""
        for subreddit in subreddits:
            helpMessage += "Subreddit: "+ subreddit + " -> **%"+subreddit+"** \n"
        await channel.send(">>> COMMANDS NSFW:\n" + helpMessage)

    for subreddit in subreddits:
        if(message.content == ("%"+subreddit.lower()) and not message.author.bot):
            channel = message.channel
            if(channel.is_nsfw()):
                i=1
                bot = RedditBot()
                sent = True
                imageList = bot.getListImage(bot.getSubReddit(subreddit),50)
                while db.exists(imageList[i],subreddit) and i<=50:
                    i+=1
                db.insertImage(imageList[i],subreddit.lower())
                await channel.send(imageList[i])

client.run(token)