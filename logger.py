from pyrogram.enums import ParseMode

from AnonXMusic import app
from AnonXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} Oynatma Kaydı</b>

<b>Chat ID :</b> <code>{message.chat.id}</code>
<b>Chat Adı :</b> {message.chat.title}
<b>Chat Kullanıcı Adı :</b> @{message.chat.username}

<b>Kullanıcı ID :</b> <code>{message.from_user.id}</code>
<b>Adı :</b> {message.from_user.mention}
<b>Kullanıcı Adı :</b> @{message.from_user.username}

<b>Sorgu :</b> {message.text.split(None, 1)[1]}
<b>Akış Türü :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return