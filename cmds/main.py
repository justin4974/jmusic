import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('1234')

    @commands.command()
    async def sayd(self, ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def rand_squad(self, ctx):
        online=[]
        for member in ctx.guild.members:
            if str(member.status) == 'online' and member.bot == False:
                online.append(member.name)
        

        random_online = random.sample(online, k=20)
        for squad in range(4):
            a = random.sample(random_online, k=5)
            await ctx.send(f"{squad+1}隊:" + str(a))
            for name in a:
                random_online.remove(name)
    
        
            


def setup(bot):
    bot.add_cog(Main(bot))
