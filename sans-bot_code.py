import time
import asyncio
from typing import Any, Union, List
from urllib.request import urlopen
import discord.client
import discord
from discord import Member
from discord.ext.commands import Bot, has_permissions
from discord.ext import commands
import random
import os
import youtube_dl
import nacl
from itertools import cycle

Client = discord.Client()
client = commands.Bot(command_prefix="s.", case_insensitive=True)
client.remove_command('help')

players = {}

queues = {}



def check_queue(id):
 if queues[id] != []:
   player = queues[id].pop(0)
   players[id] = player
   player.start()



@client.command(pass_context=True)
async def say(ctx):
    args = ctx.message.content.split(" ")
    await client.send_message(ctx.message.channel, "%s" % (" ".join(args[1:])))


@client.command(pass_context=True)
async def hi(ctx):
    messages = ["https://cdn.discordapp.com/attachments/516971396572643367/518124947944767491/undertale_box.png",
                "https://cdn.discordapp.com/attachments/516971396572643367/518107926032810005/undertale_Hi.png"]

    await client.send_message(ctx.message.channel, random.choice(messages))


@client.command(pass_context=True)
async def gm(ctx):
    Morningmessages = ['https://cdn.discordapp.com/attachments/516971396572643367/518472902538952744/undertale_box.png',
                       'https://cdn.discordapp.com/attachments/516971396572643367/518473409282310144/undertale_box_1.png']

    randomMM = random.choice(Morningmessages)

    await client.send_message(ctx.message.channel, randomMM)


@client.command(pass_context=True)
async def badtime(ctx):
    badtime = discord.Embed()
    badtime.set_image(
        url="https://cdn.discordapp.com/attachments/518850280331411466/518852785547116554/undertale_box_7.png")

    await client.send_message(ctx.message.channel, embed=badtime)


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="commands",description="",color=0x16305E)
    embed.add_field(name="s.hi", value="say hi to Sans", inline=False)
    embed.add_field(name="s.say", value="let sans say something for you!", inline=False)
    embed.add_field(name="s.badtime", value="you're gonna have a bad time", inline=False)
    embed.add_field(name="s.undertale", value="only memes about Undertale!", inline=False)
    embed.add_field(name="s.gm", value="good morning Sans", inline=False)
    embed.add_field(name="s.help_music", value="music bot commands!", inline=False)
    embed.add_field(name="s.wiki",value="Undertale wiki",inline=False)
    embed.add_field(name="s.sans_desc",value="Sans on wiki",inline=False)
    embed.set_footer(text="all text boxes were made using: https://www.demirramon.com/en/generators/undertale_text_box_generator"+" "+"If there is any bug just contact me and i will help you fix it!")
    embed.set_author(name="made by @CYBERBRAIN.java#3779")
    await client.send_message(ctx.message.author, embed=embed)


@client.command(pass_context=True)
async def help_music(ctx):
    emb = discord.Embed(title="music commands",description="",color=0x16305E)
    emb.add_field(name="s.play",value="requires: '>play'+'a youtube url'",inline=False)
    emb.add_field(name="s.play_sans", value="Megalovania", inline=False)
    emb.add_field(name="s.pause",value="pauses the current song",inline=False)
    emb.add_field(name="s.resume",value="resumes the paused song",inline=False)
    emb.add_field(name="s.stop",value="stops the current song and if there are other songs in queue it skips to the next one",inline=False)
    emb.add_field(name="s.join",value="the bot joins the current vocal chat you are in",inline=False)
    emb.add_field(name="s.leave",value="the bot leaves the current vocal chat it's in",inline=False)
    await client.send_message(ctx.message.author, embed=emb)


@client.command(pass_context=True)
async def undertale(ctx):
    imgs = os.listdir()
    randomimgs = random.choice(imgs)

    await client.send_file(ctx.message.channel, randomimgs)






@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)




@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()



@client.command(pass_context=True)
async def play(ctx,url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url,after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()


@client.command(pass_context=True)
async def play_sans(ctx):
    url = 'https://www.youtube.com/watch?v=ZcoqR9Bwx1Y'
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url,after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()



@client.command(pass_context=True)
async def pause(ctx):

 id = ctx.message.server.id
 players[id].pause()


@client.command(pass_context=True)
async def stop(ctx):

 id = ctx.message.server.id
 players[id].stop()


@client.command(pass_context=True)
async def resume(ctx):

 id = ctx.message.server.id
 players[id].resume()



@client.command(pass_context=True)
async def queue(ctx,url):

 server = ctx.message.server
 voice_client = client.voice_client_in(server)
 player = await voice_client.create_ytdl_player(url)

 if server.id in queues:

     queues[server.id].append(player)
 else:

   queues[server.id] = [player]

 await client.say('https://cdn.discordapp.com/attachments/518850280331411466/518850305144651776/undertale_box_1.png')



@client.command(pass_context=True)
async def jokes(ctx):



    jokes = ['https://cdn.discordapp.com/attachments/518850280331411466/518881623106912266/undertale_box_12.png','https://cdn.discordapp.com/attachments/518850280331411466/518881849510985768/undertale_box_13.png','https://cdn.discordapp.com/attachments/518850280331411466/518882073382223873/undertale_box_15.png','https://cdn.discordapp.com/attachments/518850280331411466/518882079606439944/undertale_box_14.png','https://cdn.discordapp.com/attachments/518850280331411466/518882301057433652/undertale_box_16.png',
          'https://cdn.discordapp.com/attachments/518850280331411466/518883557469585419/undertale_box_21.png','https://cdn.discordapp.com/attachments/518850280331411466/518883559201832981/undertale_box_17.png','https://cdn.discordapp.com/attachments/518850280331411466/518883560237826058/undertale_box_18.png','https://cdn.discordapp.com/attachments/518850280331411466/518883561412231169/undertale_box_19.png','https://cdn.discordapp.com/attachments/518850280331411466/518883563249336330/undertale_box_20.png',
          'https://cdn.discordapp.com/attachments/518850280331411466/518884130855976962/undertale_box_22.png','https://cdn.discordapp.com/attachments/518850280331411466/518884584918876190/undertale_box_23.png','https://cdn.discordapp.com/attachments/518850280331411466/518885061588811779/undertale_box_24.png','https://cdn.discordapp.com/attachments/518850280331411466/518887341318864978/undertale_box_2.png'
             ]

    randomjokes = random.choice(jokes)


    await client.send_message(ctx.message.channel,randomjokes)




@client.command(pass_context=True)
async def wiki(ctx):

    await client.send_message(ctx.message.channel,content="that's where all Undertale secrets are stored!")
    await client.send_message(ctx.message.channel, content="http://undertale.wikia.com/wiki/Main_Page")



@client.command(pass_context=True)
async def sans_desc(ctx):

    await client.send_message(ctx.message.channel,content="Hey,that's my page!")
    await client.send_message(ctx.message.channel,content="http://undertale.wikia.com/wiki/Sans")




@client.command(pass_context=True)
async def sans_battle(ctx):

    await client.send_message(ctx.message.channel,content='you wanna fight,HuH?')
    msg = await client.wait_for_message(author=ctx.message.author,timeout=50)
    if msg:
       if msg.content == 'yes':
         await client.send_message(ctx.message.channel,content="ok then.....")
         await client.send_message(ctx.message.channel,content="***YOU'RE GONNA HAVE A BAD TIME***")
         await client.send_message(ctx.message.channel,content="https://cdn.discordapp.com/attachments/518850280331411466/518896372825587732/Sanseye.gif")
       elif msg.content == 'no':
           answers = ['ok,another time...','oh.... :cry:','one day... you will pay....']
           randompick = random.choice(answers)
           await client.send_message(ctx.message.channel,content=randompick)









@client.event
async def on_ready():


    print('Logged in as')
    print('prefix = '+client.command_prefix)
    print(client.user.name)
    print(client.user.id)
    print('bot successfully started!')







client.run('')
