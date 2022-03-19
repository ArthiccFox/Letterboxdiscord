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
    film = soup.find("h4", class_="profile-statistic statistic").find("a", href=f"/{user}/films/").find("span")
    return film.string

class films_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='films')
    async def films(self, ctx, member: discord.Member):
        cursor = vscon.cursor()
        cursor.execute(f"""SELECT * FROM tb_users WHERE U_ID='{int(member.id)}'; """)
        reg = list(cursor.fetchone())

        await ctx.send(f'`{member.display_name} tem {film(reg[1])} filmes logados`')

def setup(bot):
    bot.add_cog(films_c(bot))