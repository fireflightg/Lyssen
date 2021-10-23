import discord
from discord.ext import commands
from discord.ext.commands import Bot
import youtube_dl
import soundcloud_dl
import requests
from pypresence import Presence
import asyncio
from discord import Color
import speech_recognition as sr

import time
global loop

loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)

queue = []
nows = ""
isplaying = 0
isqueue = 0
class settings:
  def _init_(self,client):
      self.client = client
      
  
class music(commands.Cog):
    #r = sr.Recognizer()
    #with sr.Microphone() as source:

      
    def _init_(self,client):
        self.client = client
        global loop

        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        

    
    #async def play_next(self,ctx):
    async def play_next(self,ctx):
      j=0
      global queue
      x = len(queue)
      while len(queue) != 0:
        x = len(queue)
        print("A")
        
        FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client
        ht = "https"
        global nows
        if ht in queue[0]:
          with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(queue[0],download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            
            nows = f"{info['title']}, ***Download here: ***{info['url']}"
            
            vc.play(source,after=lambda e: music.change(self,ctx))
            print(queue)
            queue.pop(0)
            print(queue)
            #await ctx.send(f"found it {ctx.author} is now playing {info['title']}")
            em = discord.Embed(title = "found it",description = f"{ctx.author} is now playing {info['title']}",color = Color.green())
            await ctx.send(embed = em)
        else:
          try: requests.get("".join(queue[0]))
          except: arg = " ".join(queue[0])
          else: arg = "".join(arg)
          with youtube_dl.YoutubeDL(YDL_OPTIONS ) as ydl:
            info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]      
            
          ##old stuff
          ##with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            ##info = ydl.extract_info(url,download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            
            nows = f"{info['title']}, ***Download here: ***{info['url']}"
            vc.play(source ,after=lambda e: music.change(self,ctx))
            
            print(queue)
            queue.pop(0)
            print(queue)
            #await ctx.send(f"found it {ctx.author} is now playing {info['title']}")
            em = discord.Embed(title = "found it",description = f"{ctx.author} is now playing {info['title']}",color = Color.green())
            await ctx.send(embed = em)
            while x==len(queue):
              time.sleep(1)
      async def rq(self,ctx):
        global queue
        queue.pop(0)
            
           
         
              
            
           
            
            
        


##allows bot to join
    
    def change(self,ctx):
      asyncio.run_coroutine_threadsafe(self.ready(ctx), loop)
    
    async def ready(self,ctx):
      global isplaying 
      if not queue:
        isplaying = 0
      else:
        await ctx.send("loading")

      await self.play_next(ctx)
    
      
    @commands.command(aliases=['s'])
    async def skip(self,ctx):
      await ctx.send("ok bruh im skipping")
      x = 1
      if x == 2:
        await ctx.send("error")
      else:
        if ctx.author.voice is None:
          #await ctx.send("Get in a voice channel nerd")
          em = discord.Embed(title = "No VC found",description = f"Get in a voice channel nerd")
          await ctx.send(embed = em)
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
          await voice_channel.connect()
        else:
          await ctx.voice_client.move_to(voice_channel)
        ctx.voice_client.stop()
      await self.play_next(ctx)
    
    @commands.command(aliases=['j'])
    async def join(self,ctx):
        if ctx.author.voice is None:
          #await ctx.send("Get in a voice channel nerd")
          em = discord.Embed(title = "No VC found",description = f"Get in a voice channel nerd",color = Color.red())
          await ctx.send(embed = em)
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
          await voice_channel.connect()
        else:
          await ctx.voice_client.move_to(voice_channel)
    

    @commands.command(aliases=['d', 'leave','exit'])
    async def disconnect(self,ctx):
        self.ctx.voice_client.disconnect();
    @commands.command()
    async def cypher(self,ctx,url):
      hw = "cyph3r"
      if hw in url:
        await ctx.send("So sexy ahahahhahahaha")
      else:
        await ctx.send("wrong password")
        
    @commands.command(aliases=['p','start'])
    async def play(self,ctx,url):
      global isplaying
      if isplaying == 1:
        await ctx.send("Hol up imma add it to the list")
        global queue
        queue.append(url)
        await ctx.send(f"{queue}")
      else:
        if ctx.author.voice is None:
          #await ctx.send("Get in a voice channel nerd")
          em = discord.Embed(title = "No VC found",description = f"Get in a voice channel nerd",color = Color.red())
          await ctx.send(embed = em)
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
          await voice_channel.connect()
        else:
          await ctx.voice_client.move_to(voice_channel)
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client
        ht = "https"
        global nows
        if ht in url:
          #await ctx.send("give me sec lemme find this shit")
          em = discord.Embed(title = "give me sec lemme find this shit",description = f"Searching for song",color = Color.orange())
          await ctx.send(embed = em)
          with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url,download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            
            
            nows = f"{info['title']}, ***Download here: ***{info['url']}"
            vc.play(source, after=lambda e: music.change(self,ctx))
            isplaying = 1
            #await ctx.send(f"found it {ctx.author} is now playing {info['title']}")
            em = discord.Embed(title = "found it",description = f"{ctx.author} is now playing {info['title']}",color = Color.green())
            await ctx.send(embed = em)
        else:
          try: requests.get("".join(url))
          except: arg = " ".join(url)
          else: arg = "".join(arg)
          #await ctx.send("give me sec lemme find this shit")
          em = discord.Embed(title = "give me sec lemme find this shit",description = f"Searching for song",color = Color.orange())
          await ctx.send(embed = em)
          with youtube_dl.YoutubeDL(YDL_OPTIONS ) as ydl:
            info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]      
            
          ##old stuff
          ##with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            ##info = ydl.extract_info(url,download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            
            nows = f"{info['title']}, ***Download here: ***{info['url']}"
            
            vc.play(source, after=lambda e: music.change(self,ctx))
            
            isplaying = 1
            
            #await ctx.send(f"found it {ctx.author} is now playing {info['title']}")
            em = discord.Embed(title = "found it",description = f"{ctx.author} is now playing {info['title']}",color = Color.green())
            await ctx.send(embed = em)
          
    @commands.command()
    async def next(self,ctx):
      await ctx.send("next")
      x = 1
      if x == 2:
        await ctx.send("error")
      else:
        if ctx.author.voice is None:
          await ctx.send("Loading")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
          await voice_channel.connect()
        else:
          await ctx.voice_client.move_to(voice_channel)
        ctx.voice_client.stop()
      await self.play_next(ctx)      
    @commands.command(aliases=['discord','pd'])
    async def playdiscord(self,ctx):
        if ctx.message.attachments:
          if ctx.author.voice is None:
            #await ctx.send("Get in a voice channel nerd")
            em = discord.Embed(title = "No VC found",description = f"Get in a voice channel nerd",color = Color.red())
            await ctx.send(embed = em)
          voice_channel = ctx.author.voice.channel
          if ctx.voice_client is None:
            await voice_channel.connect()
          else:
            await ctx.voice_client.move_to(voice_channel)
          ctx.voice_client.stop()
          #await ctx.send("give me sec lemme find this shit")
          em = discord.Embed(title = "give me sec lemme find this shit",description = f"Searching for song")
          await ctx.send(embed = em)
          FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
          vc = ctx.voice_client
          attachment = ctx.message.attachments[0] # gets first attachment that use 
          
          source = await discord.FFmpegOpusAudio.from_probe(f"{attachment.url}",**FFMPEG_OPTIONS)
          global nows
          nows = f"{attachment.filename}"
          vc.play(source, after=lambda e: music.change(self,ctx))
          #await ctx.send(f"found it {ctx.author} is now playing {attachment.filename}")
          em = discord.Embed(title = "found it",description = f"{ctx.author} is now playing {attachment.filename}",color = Color.green())
          await ctx.send(embed = em)
  # gets first attachment that use 
          
        else:
          #await ctx.send(f"add a file dumbass")
          em = discord.Embed(title = "No file found",description = f"Add a file dumbass" ,color = Color.red())
          await ctx.send(embed = em)

    @commands.command(aliases=['wait'])
    async def pause(self,ctx):
        #await ctx.send("Ong imagine pausing")
        em = discord.Embed(title = "Ong imagine pausing",description = f"Now pausing",color = Color.orange())
        await ctx.send(embed = em)
        
        await ctx.voice_client.pause()
  
        
    @commands.command(aliases=['r'])
    async def resume(self,ctx):
        #await ctx.send("lemme find where u were")
        em = discord.Embed(title = "lemme find where u were",description = f"Now resuming",color = Color.teal())
        await ctx.send(embed = em)
        await ctx.voice_client.resume()

    @commands.command(aliases=['version','build'])
    async def hello(self,ctx):
        em = discord.Embed(title = "Lyssen version",description = "1.0.8 BETA",color = Color.random())
        em.add_field(name = "**Author**", value = "fireflightg")
        em.add_field(name = "**invite Lyssen**", value = f"https://discord.com/api/oauth2/authorize?client_id=856614112414793748&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D856614")
        await ctx.send(embed = em)
        #await ctx.send('Hello ' f'{ctx.author} I am Lyssen bot version 1.0.8 BETA by fireflightg, invite lyssen to your server https://discord.com/api/oauth2/authorize?client_id=856614112414793748&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D856614' )
    @commands.command()
    async def stuck(self,ctx):
        await ctx.send(f'{ctx.author} here are all the commands' )
        await ctx.send("```play```"" either paste a link or search for your song by name to find and play music this will also allow for your bot to automatically join the vc your in" )
        await ctx.send("```join``` this causes the bot to join the vc your currently in" )
        await ctx.send("```pause``` pauses the music you are playing" )
        await ctx.send("```resume``` resumes the music you were playing" )
        await ctx.send("```stuck``` shows all commands" )
        await ctx.send("```hello``` replies hello and shows version and server information" )
        await ctx.send("```lyssen``` Invite lyssen to your sever https://discord.com/api/oauth2/authorize?client_id=856614112414793748&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D856614" )
        
    ##@commands.command()
    #async def testp(self,ctx):    
     # rpc = Presence("856614112414793748")
     # await rpc.connect()
     # await rpc.update(state="having fun",details="test",large_image="musik")
      
    @commands.command(aliases=['q'])
    async def queue(self,ctx):
      if not queue:
        if nows == "":
          #await ctx.send("your queue is empty bozo" )
          em = discord.Embed(title = "Your queue is empty bozo",description = f"Use ?play to add a song")
          await ctx.send(embed = em)
        else:
          em = discord.Embed(title = "Now Playing",description = f"{nows}")
          em.add_field(name = "**Next up**", value = "nothing in queue")
          await ctx.send(embed = em)




      else:
        em = discord.Embed(title = "Now Playing",description = f"{nows}")
        em.add_field(name = "**Next up**", value = f"{queue[0]}")
        em.add_field(name = "**Full List**", value = f"{queue}")
        await ctx.send(embed = em)
        #await ctx.send(f"{queue}")
        

def setup(client):
  client.add_cog(music(client))