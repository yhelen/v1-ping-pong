import discord

TOKEN = open("token.txt","r").readline()

intents = discord.Intents.default()

intents.messages = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content == '!ping':
        await message.channel.send('pong')

client.run(TOKEN)
