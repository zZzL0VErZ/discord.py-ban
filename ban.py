import discord
from discord.ext import commands

client = commands.Bot("YOUR_PREFIX")

client.remove_command("help")

@client.event
async def on_ready():
    print("Bot is online!")

@client.command()
async def ban(ctx, member: discord.Member=None, *,  reason="No Reason Given"):
    if member == None:
        return await ctx.send("Please Mention a Member!")
    elif member == ctx.author:
        return await ctx.send("You Can't Ban yourself!")
    else:
        await member.ban(reason=reason)
        embed = discord.Embed()
        embed.title="Ban Hammer!"
        embed.description=f"{ctx.author.mention} has banned {member.mention} for : \n {reason}"
        await ctx.send(embed=embed)


client.run("TOKEN")
