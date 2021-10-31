import discord
from discord.ext import commands
from modules import process_txt

class Stamp(commands.Cog):

    def __init__(self, bot, bucket):
        self.bot = bot
        self.bucket = bucket

    # 現在登録されているスタンプのフォルダ名をリストにして返す
    @commands.command(aliases=['Stamp'])
    async def stamp(self, ctx):

        await ctx.send("現在登録されているスタンプはこちらになります……")
        stamp_list = process_txt.get_stamp_list(self.bucket)
        await ctx.send(set(stamp_list))
