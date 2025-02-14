import discord
from discord.ext import commands
import shark
import asyncio
from functools import partial

bot = commands.Bot(command_prefix="shark!", intents=discord.Intents.all(), help_command=None)

@bot.command(name="money")
async def money(ctx: commands.Context):
    loop = asyncio.get_event_loop()
    moneys = await loop.run_in_executor(None, partial(shark.Economy, ctx.guild.id, ctx.author.id))
    await ctx.reply(f"お金: {moneys.money}{moneys.coin_name}")

bot.run("Token")
