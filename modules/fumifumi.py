"""
ふみふみの原点にして唯一のヤンデレ要素。制作当時はこういった部分の開発に取り組み理想のふみふみを作り上げるはずだったのにいつの間にか利便性を追求してしまった（）
"""

import discord
from discord.ext import commands
import asyncio

class Fumifumi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ふみふみ(self, ctx):
        await ctx.send("やっと私を見てくれましたね……♡")

    @commands.command()
    async def 文香さん(self, ctx):
    
        await ctx.send("文香\"さん\"？美波さんは呼び捨てなのに……？")

        def excuse(m):  # こっちが言わないと大変なことになる
            return m.content == "文香" and m.author == ctx.author

        try:  # 5秒以内に返事をするかどうかの確認
            await self.bot.wait_for("message", check=excuse, timeout=5.0)

        # 5秒のタイムアウトが発生した場合
        except asyncio.TimeoutError:
            await ctx.send("どうして私の名前を呼んではくれないのですか……？もしかして…うふふ…そういうことですか……")
            await ctx.send("Pさん……浮気は……駄目ですよ……♡")

        # 5秒以内に"文香"と返信した場合
        else:
            await ctx.send("うふふ……さっきのは聴かなかったことにしてあげます……♡")

    
    @commands.command()
    async def ありす(self, ctx):
        await ctx.send("……ありすちゃん…？いつからPさんはロリコンに？")

    @commands.command()
    async def 美波(self, ctx):
        await ctx.send("**Pさん……。美波さんと楽しそうでしたよね……？うふふ……夜道にはお気をつけて……**")

    #隠しコマンドその１
    @commands.command() 
    async def 踏んで(self, ctx):
        await ctx.send("**え、、、えい………♡　こ、、、こうですか……？**")
        await ctx.send("**P....Pさん……、、、大きくなってます……**")

    #隠しコマンドその２
    @commands.command() 
    async def 果南(self, ctx):
        await ctx.send("**ハグですか………こ、こう、、、、して、、、**")
        await ctx.send("**うふふ、、、Pさんの顔が私の胸に……どうですか？昔はこの身体が嫌だったんですけど、、、今ではすごく好きです……。Pさん、いつでも私に甘えてくださいね……♡**")

    #隠しコマンドその３
    @commands.command() 
    async def 手コキ(self, ctx):
        await ctx.send("**がんばれ♡がんばれ♡………あ、、、あれ？Pさん……もう出ちゃいそうなんですか……。うふふ…。駄目です♡　まだ我慢してくださいね……///**")

    #隠しコマンドその４
    @commands.command() 
    async def クールタチバナ(self, ctx):
        await ctx.send("ありすちゃんとお楽しみだったみたいですね……。うふふ……次は私も混ぜて下さい……♡")

    #隠しコマンドその５
    @commands.command(aliases=['Alexa', 'alexa']) 
    async def アレクサ(self, ctx):
        await ctx.send("……わ、、、、私は便利道具じゃありません………！。………でもPさんの所有物です……♡")
        await ctx.send("隠しコマンド（難易度３）") 

   