import discord
import errors
import typing
from discord.ext import commands

class Pages:
    def __init__(self,embeds:list,pageCount:int,timeout:int,loop=False:bool):
        if not isinstance(embeds,list):
            raise errors.InvaildArgument("Invaild Argument: The Arg 'embeds' must be list. not '{}'".format( type(embeds).__name__ ) )
        if not isinstance(pageCount,int):
            raise errors.InvaildArgument("Invaild Argument: The Arg 'pageCount' must be int. not '{}'".format(type(pageCount).__name__))
        if not isinstance(loop,bool):
            raise errors.InvaildArgument("Invaild Argument: The Arg 'loop' must be bool. not '{}'".format(type(loop).__name__))
        if not isinstance(timeout,int):
            raise errors.InvaildArgument("Invaild Argument: The Arg 'timeout' must be int. not '{}'".format(type(timeout).__name__))
        if len(embeds:list) == pageCount:
            raise errors.InvaildArgument("Invaild Argument: The number of args embeds must be the same as the arg pageCount.")
        else:
            self.embeds = embeds
            self.pageCount = pageCount
            self.nowPage=0
            self.loop = loop
            self.reactions = "◀ ▶ ⏭ ⏮ ⏹".split(" ")
            self.notEnded=True
    
    async def startPage(self,ctx:typing.Union([discord.Message,commands.Context]),bot:typing.Union([discord.Client,commands.Bot])):
        if isinstance(ctx,discord.Message):
            msg = ctx
            guild = msg.guild
            author = msg.author
        elif isinstance(ctx,commands.Context):
            msg = ctx.message
            guild = ctx.guild
            author = ctx.author

        async def ended(self,bot,guild):
            for react in self.reactions:
                for _ in len(self.react):
                    bot.loop.create_task.remove_reaction(react,member=guild.me)
        await ctx.send(embed=self.embeds[0])
        while True:
            if self.notEnded:
                
                def check(react,user,self):
                    emoji = str(react)
                    if self.reactions in emoji and user.id == react.message.author.id and not user.bot:
                        return True
                    else:
                        return False

                react,user = await bot.wait_for("reaction_add",check=check(react,user,self),timeout=self.timeout)
                emoji = str(react)
                if emoji == "⏹":
                    await ended()
                    break

                elif emoji == "◀":
                    if self.nowPage != 0:
                        self.nowPage -= 1
                    elif self.nowPage == 0:
                        self.nowPage = self.pageCount

                elif emoji == "▶":
                    if self.nowPage != self.pageCount:
                        self.nowPage += 1
                    elif self.nowPage == self.pageCount:
                        self.nowPage = 0

                elif emoji == "⏭":
                    if self.nowPage != self.pageCount:
                        if self.nowPage + 2 < self.pageCount:
                            self.nowPage += 2
                        else:
                            self.nowPage = self.pageCount - self.nowPage + 2

                    elif self.nowPage == self.pageCount:
                        self.nowPage = 1
                
                elif emoji == "⏮":
                    if self.nowPage != 0:
                        if self.nowPage - 2 > 0:
                            self.nowPage - 2
                        else:
                            self.nowPage = self.pageCount - self.nowPage - 2
                    elif self.nowPage == 0:
                        self.nowPage = self.pageCount
                
                await msg.remove_reaction(react,member=guild.me)
                await msg.edit(embed=self.embeds[self.nowPage])
            else:
                await ended(self,bot,guild)
                
    
    def endPage(self):
        self.notEnded=False
        return 0

    def returnPages(self):
        while self.notEnded:
            yield self.embeds


