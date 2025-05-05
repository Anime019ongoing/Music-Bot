from pyrogram import Client, filters
from yt_dlp import YoutubeDL

@Client.on_message(filters.command("play"))
async def play_music(client, message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("🎵 ɢɪᴠᴇ ᴀ ꜱᴏɴɢ ɴᴀᴍᴇ ᴛᴏ ᴘʟᴀʏ!")

    await message.reply("🔍 ꜱᴇᴀʀᴄʜɪɴɢ ꜰᴏʀ ᴍᴜꜱɪᴄ...")

    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        url = info['url']
        title = info['title']

    await message.reply(f"▶️ ᴘʟᴀʏɪɴɢ: **{title}**\n\n(ʙᴜᴛ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴀᴅᴅ ᴠᴏɪᴄᴇᴄʜᴀᴛ ꜱᴜᴘᴘᴏʀᴛ ɴᴇxᴛ)")
