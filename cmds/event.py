import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member}join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f'{member}leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('apple')

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="windwalker", url="https://www.artstation.com/windwalkerture", description="a good drawer", 
        timestamp= datetime.datetime.now())
        embed.set_author(name="justin", url="https://www.artstation.com/justin4974", icon_url="https://wiki.komica.org/images/thumb/3/35/Img15475.jpg/358px-Img15475.jpg")
        embed.set_thumbnail(url="https://cdnb.artstation.com/p/assets/images/images/029/440/571/large/windwalker-ture-ahri202008-hexie.jpg?1597564580")
        embed.add_field(name="1", value="a", inline=True)
        embed.add_field(name="2", value="b", inline=True)
        embed.add_field(name="3", value="c", inline=True)
        embed.add_field(name="4", value="d", inline=True)
        embed.set_footer(text="123456789")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))