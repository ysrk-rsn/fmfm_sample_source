"""
ふみふみbotネット環境移行バージョン(モジュール化完了後)
"""

# インストールした discord.py を読み込む
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os
from google.cloud import storage as gcs
from modules import fumifumi, fumika, import_manage, stamp, stamp_list_manage, shortcut_manage, process_txt, emoji_manage,\
                        news_manage, news,weather_manage, weather_manage, json_weather, profile_manage,profile, help_manage, other, gossip_manage


# ふみふみBotのアクセストークン（門外不出）
TOKEN = 'ここにDiscord Botトークンを入れる'

# 接続に必要なオブジェクトを生成
bot = commands.Bot(command_prefix='')  # bot はclientのサブクラス（clientクラスを継承している）

#自分のGoogle Cloud Storageに接続
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='GCPで作成したJSONファイルのPATHを入れる' 

client = gcs.Client('fumika')
bucket = client.get_bucket('fumifumi_bot')

# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print("ログインしました……♡\nLogin Name:", bot.user.name)
    print("Log in ID: ", bot.user.id)

    #デフォルトのhelpコマンドの削除
    bot.remove_command('help')

    #Cog共を追加する
    bot.add_cog(fumifumi.Fumifumi(bot))
    bot.add_cog(gossip_manage.Gossip(bot, bucket))
    bot.add_cog(fumika.Fumika(bot, client, bucket))
    bot.add_cog(import_manage.Import(bot, bucket))
    bot.add_cog(stamp_list_manage.Stamp(bot, bucket))
    bot.add_cog(shortcut_manage.Shortcut(bot, bucket))
    bot.add_cog(emoji_manage.Emoji(bot, bucket))
    bot.add_cog(news_manage.News(bot))
    bot.add_cog(weather_manage.Weather(bot))
    bot.add_cog(profile_manage.Profile(bot))
    bot.add_cog(help_manage.Helps(bot))


#コンソールにコマンドエラー文を表示させない
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if "<" in message.content:  # メッセージがカスタムスタンプを含んでいた場合
        await other.send_emoji(message, bucket)

    #スタンプのフォルダの名前に無いか探す or ショートカットコマンドの中に存在するかどうか確認する
    else:
        await other.process_others(message, bucket)

    #コマンド機能とメッセージ機能を共存させるためのコマンド
    await bot.process_commands(message)

# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)
