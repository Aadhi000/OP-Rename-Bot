# (c) @Aadhi000

from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.database import db
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command("show_thumbnail") & filters.private & ~filters.edited)
async def show_thumbnail(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sir :(")
    await add_user_to_database(c, m)
    thumbnail = await db.get_thumbnail(m.from_user.id)
    if not thumbnail:
        return await m.reply_text("𝚈𝙾𝚄 𝙳𝙸𝙳𝙽'𝚃 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻!")
    await c.send_photo(m.chat.id, thumbnail, caption="𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻!",
                       reply_markup=types.InlineKeyboardMarkup(
                           [[types.InlineKeyboardButton("𝙳𝙴𝙻𝙴𝚃𝙴 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻!",
                                                        callback_data="deleteThumbnail")]]
                       ))


@Client.on_message(filters.command("set_thumbnail") & filters.private & ~filters.edited)
async def set_thumbnail(c: Client, m: "types.Message"):
    if (not m.reply_to_message) or (not m.reply_to_message.photo):
        return await m.reply_text("𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙸𝙼𝙰𝙶𝙴 𝚃𝙾 𝚂𝙰𝚅𝙴 𝙸𝙽 𝙰𝚂 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻!!")
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await db.set_thumbnail(m.from_user.id, m.reply_to_message.photo.file_id)
    await m.reply_text("Okay,\n"
                       "𝙸 𝚆𝙸𝙻𝙻 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙸𝙼𝙰𝙶𝙴 𝙰𝚂 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻.",
                       reply_markup=types.InlineKeyboardMarkup(
                           [[types.InlineKeyboardButton("𝙳𝙴𝙻𝙴𝚃𝙴 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻!",
                                                        callback_data="deleteThumbnail")]]
                       ))


@Client.on_message(filters.command("delete_thumbnail") & filters.private & ~filters.edited)
async def delete_thumbnail(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await db.set_thumbnail(m.from_user.id, None)
    await m.reply_text("𝙾𝙺𝙰𝚈,\n"
                       "𝙸 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙵𝚁𝙾𝙼 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴.")
