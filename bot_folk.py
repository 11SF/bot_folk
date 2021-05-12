import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!!') #กำหนด Prefix
@bot.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
    print("Bot Started!") #แสดงผลใน CMD
@bot.event
async def on_message(message) : #ดักรอข้อความใน Chat
    if message.content.startswith('!!spotify') : #เมื่อข้อความในตัวแรกมีคำว่า ping
       await message.channel.send(':exclamation:ตรวจสอบค่า spotify กันด้วยนะครับ:exclamation:\nhttps://11sf.netlify.app/#/spotify/members\n@spotify family') #ข้อความที่ต้องการตอบกลับ
bot.run('ODQyMDg5NDExNTUzMzk0NzA4.YJwO4A.nnLr8NBOTeQpZdc-NcttUgd5QEA') #รันบอท (โดยนำ TOKEN จากบอทที่เราสร้างไว้นำมาวาง)