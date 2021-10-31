import discord
import asyncio
from modules import news
from discord.ext import commands


class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['News'])
    async def news(self, ctx):
        if(ctx.message.content.lower().strip() == "news"):
            news_list = news.yahoo_news_checker()
            embed = discord.Embed(title="Yahoo ニュース現在のトップニュース",
                                    description="今現在話題になっているニュースはこちらです……", color=discord.Colour.from_rgb(100, 100, 0))
            embed.set_thumbnail(
                url="https://stickershop.line-scdn.net/stickershop/v1/sticker/240346247/android/sticker.png")  # 画像のサムネイル
            for i in range(len(news_list)):
                current_dict = news_list[i]
                embed.add_field(
                    name=current_dict['title'], value=current_dict['link'], inline=False)
            await ctx.send(embed=embed)

        else:
            char_list = ctx.message.content.split()
            found = False
            if(len(char_list) == 2):
                news_site = char_list[1]
                if(news_site == "yahoo"):
                    news_list = news.yahoo_news_checker()
                    embed = discord.Embed(title="Yahoo ニュース現在のトップニュース",
                                            description="今現在話題になっているニュースはこちらです……", color=discord.Colour.from_rgb(100, 100, 0))
                    found = True

                elif(news_site == "gigazine"): # GIGAZINEの場合
                    news_list = news.gigazine_news_checker()
                    embed = discord.Embed(title="GIGAZINE ニュース現在のトップニュース",
                                            description="今現在話題になっているニュースはこちらです……", color=discord.Colour.from_rgb(100, 100, 0))
                    found = True

                elif(news_site == "lovelive"): # loveliveの場合
                    news_list = news.lovelive_news_checker()
                    embed = discord.Embed(title="ラブライブ! 新着SS情報",
                                            description="ラブライブの新着SSはこちらです……", color=discord.Colour.from_rgb(100, 100, 0))
                    found = True

                elif(news_site == "vipper"): # loveliveの場合
                    news_list = news.vipper_news_checker()
                    embed = discord.Embed(title="VIPPERな俺 新着スレ情報",
                                            description="VIPPERな俺の新着スレはこちらです……", color=discord.Colour.from_rgb(100, 100, 0))
                    found = True

                if(found):
                    embed.set_thumbnail(
                        url="https://stickershop.line-scdn.net/stickershop/v1/sticker/240346247/android/sticker.png")  # 画像のサムネイル
                    for i in range(len(news_list)):
                        current_dict = news_list[i]
                        embed.add_field(
                            name=current_dict['title'], value=current_dict['link'], inline=False)

                    await ctx.send(embed=embed)

                else:
                    await ctx.send("申し訳ございません……。そちらのサイトには対応しておりません…。詳細は\"help news\"をご参照下さい……")

            else:
                await ctx.send("引数の数が正しくありません……。詳細は\"help news\"をご参照下さい……")
