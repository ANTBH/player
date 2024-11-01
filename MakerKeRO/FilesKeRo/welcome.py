import os
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram import Client, emoji 
from pyrogram import filters

#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
@Client.on_message(filters.new_chat_members)
async def wel__come(client: Client, Message):
	chatid= message.chat.id
	await client.send_message(text=f"- نورت يا ياحلو 🌚♥ \n احترم الادمنيه ✨ \n تفاعل وخذ بوسه  {message.from_user.mention}\n│ \n└ʙʏ في {message.chat.title}",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def good_bye(client: Client, Message):
	chatid= message.chat.id
	await client.send_message(text=f"- يلا فدوه يا حبيبي لا تجي من جديد♥\n│ \n└ʙʏ  {message.from_user.mention} ",chat_id=chatid)
	
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//