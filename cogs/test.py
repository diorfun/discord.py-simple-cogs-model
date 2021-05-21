import discord
from discord.ext import commands
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown
import random
import time
import datetime
import asyncio
import json




class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


     #HI! you cand find here 3 basic commands ping, choose and say

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user) #use one time (1) to get (10) seconds cooldown per user you can edit them whatever you want
    async def say(self, ctx, *, say=None):
        if say:
            alm = discord.AllowedMentions(users=False, everyone=False, roles=False)
            await ctx.send(f'{say}', allowed_mentions=alm)
        elif say == None:
            embed = discord.Embed(title=f'<:error:754413108822409386>**|**ERROR',
                                  description=f"<:x_:754406625560756274>**|{self.bot.prefix}say**\n<:0_:754406673564696637>**|{self.bot.prefix}say (mesaj)**\n<:hmm:754410711828004948>**|{self.bot.prefix}say #traiescfun**",
                                  colour=discord.Colour.blue())

            await ctx.send(embed=embed)

    @commands.command()
    async def choose(self, ctx, *choices: str):
        embed = discord.Embed(title='Grea decizie...', description=f'**O sa aleg** ****{(random.choice(choices))}****', colour=0x00ffee)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(2, 8, commands.BucketType.user)
    async def ping(self, ctx):
        now = time.time_ns()/1e6
        msg = await ctx.send("🏓")
        send_time = time.time_ns()/1e6
        embed = discord.Embed(title = '🏓Pong!', description = (f'Bot latency:{round(self.bot.latency * 1000)} ms\nREST latency:{round(send_time - now)} ms'),color = 0x62016f)
        await msg.edit(content=None, embed=embed)



def setup(bot):
    bot.add_cog(Fun(bot))
