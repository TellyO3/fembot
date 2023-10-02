import json
import os
import re

import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

pattern = re.compile("s+l+a+y+")


def load_config():
    if os.path.isfile("config.json"):
        file = open("config.json", "r")
        return json.load(file)
    else:
        print("Config.json not found! Create it using the default config provided!")


config = load_config()


async def send_reaction(message):
    reaction_list = config["reaction_list"]
    reaction_link = random.choice(reaction_list)
    await message.channel.send(reaction_link)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "<@1155264218770186370>" in message.content:
        await send_reaction(message)
    else:
        random_number = random.randint(0, config["reaction_chance"])
        if random_number == 1:
            await send_reaction(message)

    if pattern.search(message.content.lower()):
        await message.add_reaction("💅")


bot_token = os.getenv("BOT_TOKEN")
if not type(bot_token) == str:
    bot_token = config["bot_token"]
client.run(bot_token)
