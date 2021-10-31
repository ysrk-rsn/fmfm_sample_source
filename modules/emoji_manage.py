import discord 
import asyncio
import os
import re
from modules import process_txt
from discord.ext import commands

def isalnum(s):
    alnumReg = re.compile(r'^[a-zA-Z0-9]+$')
    return alnumReg.match(s) is not None

class Emoji(commands.Cog):
    def __init__(self, bot, bucket):
        self.bot = bot
        self.bucket = bucket
        
    #カスタム絵文字の登録
    @commands.command()
    async def emoji(self, ctx):
        char_set = ctx.message.content.split()
        if(len(char_set) == 2):
            emoji_list = []
            for i in ctx.guild.emojis:
                emoji_list.append(i.name)

            #現在登録されているカスタム絵文字のリストを送信
            if(char_set[1] == "list"):

                remainder = 50 - len(emoji_list)
                text = "現在登録されているカスタム絵文字はこちらです……\n登録数: " + str(len(emoji_list)) + "\n残存登録枠: " + str(remainder)
                await ctx.send(text)
                await ctx.send(emoji_list)
            
            #新たに絵文字の登録を行う
            else:

                if(char_set[1] in emoji_list): #カスタム絵文字に既に登録されている場合
                    path = process_txt.search_shortcut(char_set[1].lower(), self.bucket)
                    await ctx.send("そちらのスタンプは既にカスタム絵文字に登録されています....")
                    blob = self.bucket.get_blob(path)
                    blob.download_to_filename('./emoji.png')
                    await ctx.send(file=discord.File('./emoji.png'))
                    os.remove('./emoji.png')

                else: #登録プロセス
                    path = ""
                    path = process_txt.search_shortcut(char_set[1].lower(), self.bucket)
                    if(path != ""):
                        blob = self.bucket.get_blob(path)
                        blob.download_to_filename('./emoji.png')
                        await ctx.send("こちらのスタンプをカスタム絵文字に登録いたしますか...？(yes / no で回答して下さい……)",file=discord.File('./emoji.png'))

                        def check(m):
                            return m.author == ctx.author

                        try:
                            answer = await self.bot.wait_for("message", check=check, timeout=20.0)

                        except asyncio.TimeoutError:
                            await ctx.send("タイムアウトしました")
                            os.remove('./emoji.png') #ファイルを送信後にファイルを消去)

                        else:
                            if answer.content.lower().strip() == "yes": #回答が'yes"だった場合
                                if(isalnum(char_set[1].lower())): #絵文字に登録できるものであるかどうかの確認
                                    with open('./emoji.png', 'rb') as fd: #ファイルをバイナリモードで読み込む
                                        await ctx.guild.create_custom_emoji(name=char_set[1].lower(), image=fd.read()) #カスタム絵文字の追加

                                    await ctx.send("カスタム絵文字の作成に成功しました……")
                                    os.remove('./emoji.png') #ファイルを送信後にファイルを消去)

                                else: #日本語等カスタム絵文字に使用できない文字が含まれている場合にエラー分を返す
                                    await ctx.send("絵文字にはアルファベットと数字で表示されるものしか登録ができません……。登録のためにはショートカット名を変更して下さい……")
                                    os.remove('./emoji.png')

                            else:
                                await ctx.send("絵文字の登録をキャンセルしました……")
                                os.remove('./emoji.png') #ファイルを送信後にファイルを消去)

                    else: #指定したパスが存在しない場合に返す
                        await ctx.send("ご指定されたスタンプのショートカットがありません……")

        else:
            await ctx.send("引数の数が正しくありません……。こちらのコマンドの引数は２つです……")