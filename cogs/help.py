from discord.ext import commands
import discord

class help_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        file = discord.File('./img/help.png', filename='help.png')
        embed = discord.Embed(title="comandos")
        embed.add_field(name='t?reg [nick]', value=' no lugar do nick coloque o que aparece no link')
        embed.add_field(name='t?films [@ do usuario]', value='mostra todos os filmes que a pessoa ja logou')
        embed.add_field(name='t?yfilms [@ do usuario]', value='mostra todos os filmes que a pessoa ja logou esse ano')
        embed.add_field(name='t?ratedfilms [@ do usuario]', value='mostra todos os filmes que a pessoa logou com avaliação')
        await ctx.send(file=file, embed=embed)

def setup(bot):
    bot.add_cog(help_c(bot))