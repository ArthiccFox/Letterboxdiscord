from discord.ext import commands
import sqlite3
import discord
import requests
from bs4 import BeautifulSoup

def dataconnect():
    path = f"./users/users.db"
    con = sqlite3.connect(path)
    return con
vscon = dataconnect()

def film(user):
    html = requests.get(f"https://letterboxd.com/{user}/").content
    soup = BeautifulSoup(html, 'html.parser')
    film = soup.find("a", href=f"/{user}/films/diary/for/2022/").find("span").string
    return film.string

class yfilms_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='yfilms')
    async def yfilms(self, ctx, member: discord.Member):
        cursor = vscon.cursor()
        cursor.execute(f"""SELECT * FROM tb_users WHERE U_ID='{int(member.id)}'; """)

        if cursor.fetchone() != None:
            reg = list(cursor.fetchone())

            await ctx.send(f'`{member.display_name} tem {film(reg[1])} filmes logados nesse ano`')
        else:
            ctx.send('esse usuario nao esta registrado, use t?help')

def setup(bot):
    bot.add_cog(yfilms_c(bot))