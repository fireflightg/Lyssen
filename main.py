import discord
from discord.ext import commands
from discord import Color
import music

cogs = [music]
client = commands.Bot(command_prefix ='?',intents = discord.Intents.all())
client.remove_command("help")
for i in range(len(cogs)):
  cogs[i].setup(client)
@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help",description = "Use ?help <command> for extended info")
  em.add_field(name = "Play Commands", value = "play,playdiscord")
  em.add_field(name = "Call Commands", value = "join,disconnect,pause,resume")
  em.add_field(name = "Queue Commands", value = "queue,skip")
  em.add_field(name = "Version info", value = "hello")
  
  await ctx.send(embed = em)
  @help.command()
  async def play(ctx):
    em = discord.Embed(title = "Play",description = "Plays audio from both youtube and soundcloud")
    em.add_field(name = "**Syntax**", value = "?play <url or name>")
    em.add_field(name = "**aliases**", value = "p,play,start")
    await ctx.send(embed = em)
  @help.command()
  async def playdiscord(ctx):
    em = discord.Embed(title = "playdiscord",description = "Plays audio from an mp3 file")
    em.add_field(name = "**Syntax**", value = "?playdiscord <upload mp3 file>")
    em.add_field(name = "**aliases**", value = "pd,playdiscord,discord")
    await ctx.send(embed = em)
  @help.command()
  async def join(ctx):
    em = discord.Embed(title = "Join",description = "Joins the bot to the voice channel you are currently in")
    em.add_field(name = "**Syntax**", value = "?join")
    em.add_field(name = "**aliases**", value = "j,join")
    await ctx.send(embed = em)
  @help.command()
  async def disconnect(ctx):
    em = discord.Embed(title = "Disconnect",description = "Disconnects the bot from the voice channel")
    em.add_field(name = "**Syntax**", value = "?disconnect")
    em.add_field(name = "**aliases**", value = "d,disconnect,leave,exit")
    await ctx.send(embed = em)
  @help.command()
  async def pause(ctx):
    em = discord.Embed(title = "Pause",description = "Pauses whatever audio is playing")
    em.add_field(name = "**Syntax**", value = "?pause")
    em.add_field(name = "**aliases**", value = "pause,wait")
    await ctx.send(embed = em)
  @help.command()
  async def resume(ctx):
    em = discord.Embed(title = "Resume",description = "Resumes any audio that has been paused")
    em.add_field(name = "**Syntax**", value = "?resume")
    em.add_field(name = "**aliases**", value = "resume,r")
    await ctx.send(embed = em)
  @help.command()
  async def queue(ctx):
    em = discord.Embed(title = "Queue",description = "Shows all items in your queue")
    em.add_field(name = "**Syntax**", value = "?queue")
    em.add_field(name = "**aliases**", value = "queue,q")
    await ctx.send(embed = em)
  @help.command()
  async def skip(ctx):
    em = discord.Embed(title = "Skip",description = "Skip the next song in your queue")
    em.add_field(name = "**Syntax**", value = "?skip")
    em.add_field(name = "**aliases**", value = "skip,s")
    await ctx.send(embed = em)


client.run("ODU2NjE0MTEyNDE0NzkzNzQ4.YNDmDw.0VNSMXQFobtq27AsUtkgtnvpU9g")