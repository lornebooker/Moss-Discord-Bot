import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "m-")

insults = ['Im not saying I hate you, but I would unplug your life support to charge my phone.', 'I am jealous of all the people that have not met you!', 'Do you still love nature, despite what it did to you?', 'Oh my God, look at you. Was anyone else hurt in the accident?', 'Your face makes onions cry.', 'You are living proof that evolution can go in reverse.', 'Im blonde, whats your excuse?']
#chatFilter = ['Lorne is the best', 'life']

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message) :
#    messageContents = message.content.split(" ")
#    for word in messageContents:
#        if word.upper() in chatFilter:
            # Code here only activates if any words are used that are in the chatFilter list
            #await client.delete_message(message)
#            await client.send_message(message.channel, "**Oops...** You may have used some words that are not allowed, to see which words are not allowed, type in (n-filterlist)")

    
    if message.content.upper().startswith('m-INSULT'):
        userID = message.author.id
        await client.send_message(message.channel, ("<@%s> " % (userID)) + (random.choice(insults)))
        await client.delete_message(message)

    if message.content.upper().startswith('m-SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        await client.delete_message(message)

    if message.content.upper().startswith('m-JOKE'):
        userID = message.author.id
        await client.send_message(message.channel, ("<@%s> " % (userID)) + ("I was coded by Lorne, you think I can tell jokes :laughing:"))
        await client.delete_message(message)

client.run("NDIzOTE3MjA3OTM2OTU4NDY2.DZUnCg.Vs6H4jt4STM-2TbqkDTCmxExdPU")
