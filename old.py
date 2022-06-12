import os
from time import sleep
import discord
import random
TOKEN = os.environ['TOKEN']
PREFIX = ";"
client = discord.Client()
rare_crate_items = ["octane", "fennec", "takumi", "masamune", "jäger 619"]
paints = ["Titanium white ", "Burnt sienna ", "Crimson ", "Cobalt ", "Purple ", "Forest green ", "Pink ", "Grey ", "Sky blue ", "Orange ", "Black ", "Saffron ", "Lime ", "Unpainted ", "Unpainted ","Unpainted ","Unpainted ","Unpainted "]

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == 975450692053499904:
      if message.content.startswith(f'{PREFIX}crate daily'):
        item = random.choice(paints) +random.choice(rare_crate_items)
        await message.channel.send("Opening daily rare crate...")
        sleep(3)
        await message.channel.send(f"Your item is: {item}!")
      if message.content == f'{PREFIX}crate' or message.content == f'{PREFIX}crate help':
          await message.channel.send("\nHelp \nUse ;crate daily for your daily crate!")

# Add timer for users

client.run(TOKEN)