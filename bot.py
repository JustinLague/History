import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

users = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
    welcomerChannel = [channel for channel in guild.text_channels if channel.name == "welcomer"][0]

    userData = getUserData(await welcomerChannel.history().flatten())

    print(list(userData))


def getUserData(messages):
    for message in messages:
        if users[message.author] == None:
            users[message.author] = MessageData


client.run(TOKEN)


class MessageData:
  def __init__(self, author, datetime, message):
    self.author = author
    self.datatime = datetime
    self.lastJoinMessage = message