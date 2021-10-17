import discord
import random
import praw
import reddit
import random
from random import randint
from discord.ext import commands
from discord import DMChannel
import time
from datetime import datetime


global prefix1
prefix1 = "a!"
client = commands.Bot(command_prefix = prefix1)
client.remove_command('help')
customstat = 'a!help'
 
global overclock
overclock = ""

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=customstat))
  print('Bot has initialized.')
  
@client.command()
async def help(ctx):
  embed=discord.Embed(title="Commands", description="All the available commands AniBOT can recognize", color=0xff0000)
  embed.set_author(name="AniBOT")
  embed.add_field(name="help", value="Displays all the valid commands (**this embed**).", inline=True)
  embed.add_field(name="ping", value="Shows the latency of the connection between AniBOT and the current server the command was executed from.", inline=True)
  embed.add_field(name="ani {'subreddit'}", value="Obtains an image from subreddit on Reddit specified by the user.", 
  inline=True)
  embed.set_footer(text="Sent by AniBOT, Developed by Sahil and Yatin Jason")
  await ctx.send(embed=embed)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="help command"))
  time.sleep(5)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=customstat))


@client.command()
@commands.has_permissions(administrator=True)

async def purge(ctx, pamount):
  await ctx.channel.purge(limit=int(pamount))

  reddit=praw.Reddit(client_id = "Rrl9A7wNiRtR6w",
                  client_secret = "bm-GUeidyX5coIbPeGVZwll4NfIZuQ",
                  username = "HorizonZoom",
                  password = "Bowling@1",
                  user_agent = "Watson")



@client.command()
async def ani(ctx, str_sub):

  await ctx.send("Getting image from **r/"+ str(str_sub)+"**...")
  subreddit = reddit.subreddit(str_sub)
  all_subs = []
  top = subreddit.top(limit =50)

  for submission in top:
      all_subs.append(submission)

  random_sub = random.choice(all_subs)

  url = random_sub.url

  embed=discord.Embed(
      
      title=random_sub.url, 
      
  )

  embed.set_image(url=url)

  embed.set_author(name="AniBOT")



  embed.set_footer(text="Reddit API accessed by AniBOT")
  await ctx.channel.purge(limit=1)


  await ctx.send(embed=embed)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=customstat))


@client.command()
async def lions(ctx):


  await ctx.send("Getting image from **r/lions**...")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Retrieving data from Reddit API"))
  subreddit = reddit.subreddit("lions")
  all_subs = []
  top = subreddit.top(limit =50)

  for submission in top:
      all_subs.append(submission)

  random_sub = random.choice(all_subs)

  url = random_sub.url

  embed=discord.Embed(
      
      title=random_sub.url, 
      
  )

  embed.set_image(url=url)

  embed.set_author(name="AniBOT")



  embed.set_footer(text="Reddit API accessed by AniBOT")
  await ctx.channel.purge(limit=1)


  await ctx.send(embed=embed)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=customstat))

    





@client.command()
async def ping(ctx):

  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Calculating latency between AniBOT and server."))
  time.sleep(1)
  await ctx.send(f"The estimated latency on this server's connection with AniBOT is **{round(client.latency * 1000)}ms**")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=customstat))


  




    






  
      



  
  

       

    
    










client.run('ODk5MzM0MTM1MzQzMTA4MTU3.YWxQLg.V3jtls8sqz_xY_jGFaiMsAq9JaQ')

                 
