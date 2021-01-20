from discord.ext import commands
from GoodByeCorona import Corona

bot = commands.Bot(command_prefix='./')
key = 'Your Api Key'

@bot.command()
async def Corona(ctx):
    data = Corona(key)
    res1 = await data.DomesticCounter()
    res2 = await data.CityOccurrence()
    await ctx.send('아무거나 보내보세요')


bot.run('Your Token')