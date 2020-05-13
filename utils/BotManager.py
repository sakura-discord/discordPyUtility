import discord
from discord.ext import commands
import os
import sys

class BotManagement(commands.Cog):
    def __init__(self,bot,directory:str=None):
        self.bot = bot
        self.dir = directory
    
    @commands.command(description="Botを再起動します。",aliases=["restart","reboot"])
    async def rebootBot(self,ctx):
        await ctx.send("再起動します…")
        os.execl(sys.executable, sys.executable, *sys.argv)

    @commands.command(description="Botをログアウトさせます。",aliases=["logout","shutdown","close","cu"])
    async def shutdownBot(self,ctx):
        await ctx.send("ログアウトします。")
        await self.bot.close()
    
    @commands.command(description="拡張機能(Cog)を再読み込みします。",aliases=["reload","rl"])
    async def reloadExtention(self,ctx,extName):
        try:
            self.bot.reload_extention("{}".format(extName) if not self.dir else "{}.{}".format(self.dir,extName))
        except Exception as e:
            errorText=("```"
            "{}".format(e)
            "```"
            )
            await ctx.author.send(errorText)
        else:
            await ctx.send("再読み込みしました！")
    
    @commands.command(description="拡張機能(Cog)の読み込みを解除します",aliases=["unload","ul"])
    async def unloadExtention(self,ctx,extName):
        try:
            self.bot.unload_extention("{}".format(extName) if not self.dir else "{}.{}".format(self.dir,extName))
        except Exception as e:
            errorText=("```"
            "{}".format(e)
            "```"
            )
            await ctx.author.send(errorText)
        else:
            await ctx.send("読み込みを解除しました！")
    
    @commands.command(description="拡張機能(Cog)を読み込みます。",aliases=["load"])
    async def loadExtention(self,ctx,extName):
        try:
            self.bot.unload_extention("{}".format(extName) if not self.dir else "{}.{}".format(self.dir,extName))
        except Exception as e:
            errorText=("```"
            "{}".format(e)
            "```"
            )
            await ctx.author.send(errorText)
        else:
            await ctx.send("読み込みました！")
def setup(bot,dir_=None):
    if dir_:
        bot.add_cog(BotManagement(bot,dir_))
    else:
        bot.add_cog(BotManagement(bot))