from telethon import TelegramClient, events
import os
import asyncio

api_id = 38075627
api_hash = '8430051afb4f0a363c9de1ee2195518b'
phone = '+201515483289'
bot_token = '8498758800:AAExV8E9jNglOfryOEQyWQsFlqwdxEntVOk'
destination = 'VIP'   # قناتك الخاصة

user = TelegramClient('user_session', api_id, api_hash)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

active_tasks = {}

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply(
        "البوت شغال يا وحش! 🔥\n\n"
        "/install رابط → فيديو واحد بس\n"
        "install all رابط → كل الفيديوهات اللي تحتها\n"
        "/stop → إيقاف"
    )

@bot.on(events.NewMessage(pattern=r"/install(?:\s+all)?\s+(.+)"))
async def install(event):
    all_mode = 'all' in event.pattern_match.group(0)
    url = event.pattern_match.group(1).strip()
    # باقي الكود زي ما كتبته قبل كده (هبعتهولك كامل في الرسالة الجاية لو عايز)

async def main():
    await user.start(phone=phone)
    await bot.run_until_disconnected()

with user:
    user.loop.run_until_complete(main())
  


