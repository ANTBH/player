from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "عبد المجيد",
    api_id="12847352",
    api_hash="19b76e60ee49e2356497d361cabcf7a8",
    bot_token="8174158596:AAHWO_rXQuJF-ogWeIsxaFvYJxg_297hQv8",
    plugins=dict(root="J_dd_J")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    USER = "J_dd_J"
    await bot.send_message(USER, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
