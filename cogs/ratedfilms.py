import requests
import discord
from bs4 import BeautifulSoup
from discord.ext import commands
import sqlite3

def dataconnect():
    path = f"./users/users.db"
    con = sqlite3.connect(path)
    return con
vscon = dataconnect()

def ratedfilm(user):
    html = requests.get(f"https://letterboxd.com/{user}/").content
    soup = BeautifulSoup(html, 'html.parser')
    ratedlogs = soup.find("a", class_="all-link", href=f"/{user}/films/ratings/by/rating/")
    return ratedlogs.string


class rated_c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    @commands.command(name='ratedfilms')
    async def ratedfilms(self, ctx, member: discord.Member):  
        cursor = vscon.cursor()
        cursor.execute(f"""SELECT * FROM tb_users WHERE U_ID='{int(member.id)}'; """)

        if cursor.fetchone() != None:
            reg = list(cursor.fetchone())
            
            await ctx.send(f'`{member.display_name} tem {ratedfilm(reg[1])} filmes logados (com rate)`')
        else:
            await ctx.send('esse usuario nao esta registrado, use t?help')

def setup(bot):
    bot.add_cog(rated_c(bot))