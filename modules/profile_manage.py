import discord 
from modules import profile
from discord.ext import commands

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 各キャラクターのプロフィール情報をEmbedにして送信する
    @commands.command(aliases=['Profile'])
    async def profile(self, ctx):
        char_list = ctx.message.content.split()
        if(len(char_list) != 2):
            await ctx.send("引数の数が正しくありません……。詳細は\"help profile\"をご参照下さい……")

        else:
            name = char_list[1]
            idol_data = profile.get_idol_profile(name)
            if(idol_data.empty):
                await ctx.send("そちらのデータは存在しません……。入力ミスがございませんか……？")

            else:
                embed = discord.Embed(title="**アイドル大百科**",
                                        description="**Pさん……私ので良ければいくらでも教えますよ……**")
                column_list = idol_data.columns.values
                for i in range(len(idol_data.columns)):
                    if(i in (0, 1, 3, 4, 7, 8, 9)):
                        embed.add_field(
                            name=column_list[i], value=idol_data.iloc[0, i])

                    else:
                        embed.add_field(
                            name=column_list[i], value=idol_data.iloc[0, i], inline=False)

                await ctx.send(embed=embed)

                if(name == "木下翔太郎"):
                    await ctx.send(f"{ctx.author.mention} それにしても、なぜこれを入力したし………隠しコマンド(難易度２)")

                elif(name == "ケビン"):
                    await ctx.send(f"{ctx.author.mention} いや、本当なんでこれがあると思ったんだ……（難易度４）")

                elif(name == "郡道美玲" or name == "郡道"):
                    await ctx.send(f"{ctx.author.mention} 狂気の沙汰だよ……これを見つけるなんて………（難易度５　-最高難易度-）")
