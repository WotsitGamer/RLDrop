print("SUP")
import discord
from discord.ext import commands
import os
from time import sleep
import random
import time
from discord.ext.commands import cooldown, BucketType
rare_crate_items = ["octane", "fennec", "takumi", "masamune", "jäger 619"]
paints = ["Titanium white ", "Burnt sienna ", "Crimson ", "Cobalt ", "Purple ", "Forest green ", "Pink ", "Grey ", "Sky blue ", "Orange ", "Black ", "Saffron ", "Lime ", "Unpainted ", "Unpainted ","Unpainted ","Unpainted ","Unpainted "]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=';', intents=intents)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def daily(ctx):
  if ctx.channel.id == 975450692053499904:
    item = random.choice(paints) + random.choice(rare_crate_items)
    await ctx.channel.send("Opening daily rare crate...")
    sleep(3)
    await ctx.channel.send(f"Your item is: {item}!")
@bot.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
def run():
  bot.run(os.environ["TOKEN"])
if __name__ == "__main__":
  run()

