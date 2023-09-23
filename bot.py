import json
import os

import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


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
    elif message.content.startswith("<@1155264218770186370>"):
        await send_reaction(message)
    else:
        random_number = random.randint(0, config["reaction_chance"])
        if random_number == 1:
            await send_reaction(message)


bot_token = ""
if len(os.getenv("BOT_TOKEN")) == 72:
    bot_token = os.getenv("BOT_TOKEN")
else:
    bot_token = config["bot_token"]
client.run(bot_token)
