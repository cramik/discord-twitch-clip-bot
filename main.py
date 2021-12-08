import subprocess
import os
import discord

TOKEN = ""

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if "https://clips.twitch.tv/" in message.content:
    output = subprocess.Popen(["python3", "twitch-dl.pyz", "download", "-q", "source", message.content], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
    downloadpos = output.find('Downloaded: ')
    if downloadpos != -1:
        filenamestart = downloadpos+12
        length = len(output)
        filename = output[filenamestart-length:][:-2]
        await message.channel.send(file=discord.File('./' + filename))
        
client.run(TOKEN)
