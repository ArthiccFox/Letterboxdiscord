from discord.ext import commands
import sqlite3


class reg_c(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reg')
    async def reg(self, ctx, letteruser):
        path = f"./users/users.db"
        con = sqlite3.connect(path)
        author = ctx.message.author
        registro=f"""INSERT INTO tb_users 
                (U_ID, U_LETTERUSER)
            VALUES('{author.id}','{letteruser}')"""

        c = con.cursor()
        c.execute(registro)
        con.commit()
        print(f'registro inserido de {author.name}')
        await ctx.send('voce registrou')
def setup(bot):
    bot.add_cog(reg_c(bot))