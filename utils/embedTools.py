import discord
import errors

class embedBuilder:
    #これ書いてるとき気が狂いそうだったわ
    def __init__(self,**kwargs):
        self.title=kwargs.get("title","")
        self.description=kwargs.get("description","")
        self.color=kwargs.get("color",)

        self.authorName=kwargs.get("authorName","None")
        self.authorIconURL=kwargs.get("authorIcon","None")
        self.footerText=kwargs.get("footerText","None")
        self.footerIcon=kwargs.get("footerIcon","None")
        self.timestamp=kwargs.get("timestamp","None")
        self.thumbnailURL=kwargs.get("thumbnailURL","None")
        self.imageURL=kwargs.get("imageURL","None")

        self.embed=discord.Embed()
        self.embed.title=self.title
        self.embed.description=self.description
        if self.authorName:
            if authorIconURL:
                self.embed.set_author(name=self.authorName,icon_url=self.authorIconURL)
            else:
                self.embed.set_author(name=self.authorName)
        if self.footerText:
            if self.footerIcon:
                self.embed.set_footer(text=self.footerText,icon_url=self.footerIcon)
            else:
                self.embed.set_footer(text=self.footerText)
        if self.timestamp:
            self.embed.timestamp = self.timestamp
        if self.thumbnailURL:
            self.embed.set_thumbnail(url=self.thumbnailURL)
        if self.imageURL:
            self.embed.set_image(url=self.imageURL)

        self.changes={}
    
    def addField(name:str,value:str):
        self.embed.add_field(name=name,value)
        return self.embed
    
    def addFieldByList(fields:list):
        if isinstance(fields[0],list) and isinstance(fields,list):
            dictFields=dict(fields)
            for k,v in dictFields.items():
                self.embed.add_field(name=k,value=v)
        else:
            raise errors.InvaildArgument("Arg fields syntax is '[['fieldName','fieldValue'],['fieldName','fieldValue']]'")
    
    def addFieldByDict(fields:dict):
        if isinstance(fields,dict):
            for k,v in fields.items()
                self.embed.add_field(name=k,v)
        else:
            raise errors.InvaildArgument("Arg fields syntax is '{'fieldName':'fieldValue','fieldName':'fieldValue'}'")

    def build(self):
        return self.embed