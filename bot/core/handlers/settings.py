# (c) @AbirHasan2005

import asyncio
from pyrogram import types, errors
from configs import Config
from bot.core.db.database import db


async def show_settings(m: "types.Message"):
    usr_id = m.chat.id
    user_data = await db.get_user_data(usr_id)
    if not user_data:
        await m.edit("Failed to fetch your data from database!")
        return
    upload_as_doc = user_data.get("upload_as_doc", True)
    caption = user_data.get("caption", None)
    apply_caption = user_data.get("apply_caption", True)
    thumbnail = user_data.get("thumbnail", None)
    buttons_markup = [
        [types.InlineKeyboardButton(f"𝚄𝙿𝙻𝙾𝙰𝙳𝙴𝙳 𝙰𝚂 𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃 {'✅' if upload_as_doc else '🗑️'}",
                                    callback_data="triggerUploadMode")],
        [types.InlineKeyboardButton(f"𝙰𝙿𝙿𝙻𝚈 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 {'✅' if apply_caption else '🗑️'}",
                                    callback_data="triggerApplyCaption")],
        [types.InlineKeyboardButton(f"𝙰𝙿𝙿𝙻𝚈 𝙳𝙴𝙵𝙰𝚄𝙻𝚃 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 {'🗑️' if caption else '✅'}",
                                    callback_data="triggerApplyDefaultCaption")],
        [types.InlineKeyboardButton("𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽",
                                    callback_data="setCustomCaption")],
        [types.InlineKeyboardButton(f"{'Change' if thumbnail else 'Set'} Thumbnail",
                                    callback_data="𝚂𝙴𝚃 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻")]
    ]
    if thumbnail:
        buttons_markup.append([types.InlineKeyboardButton("𝚂𝙷𝙾𝚆 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻",
                                                          callback_data="showThumbnail")])
    if caption:
        buttons_markup.append([types.InlineKeyboardButton("𝚂𝙷𝙾𝚆 𝙲𝙰𝙿𝚃𝙸𝙾𝙽",
                                                          callback_data="showCaption")])
    buttons_markup.append([types.InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴",
                                                      callback_data="closeMessage")])

    try:
        await m.edit(
            text="**-𝙲𝚄𝚂𝚃𝙾𝙼𝙸𝚉𝙴 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂-**",
            reply_markup=types.InlineKeyboardMarkup(buttons_markup),
            disable_web_page_preview=True,
            parse_mode="Markdown"
        )
    except errors.MessageNotModified: pass
    except errors.FloodWait as e:
        await asyncio.sleep(e.x)
        await show_settings(m)
    except Exception as err:
        Config.LOGGER.getLogger(__name__).error(err)
