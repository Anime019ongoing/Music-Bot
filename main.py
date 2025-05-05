from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("𝙈ᴜꜱɪᴄ_ʙᴏᴛ", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

# Load plugins
import plugins.play

print("✅ ᴍᴜꜱɪᴄ ʙᴏᴛ ɪꜱ ꜱᴛᴀʀᴛɪɴɢ...")
app.start()
pytgcalls.start()
print("✅ ʙᴏᴛ ɪꜱ ʀᴜɴɴɪɴɢ...")
app.idle()
