# (c) @Aadhi000
from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sir :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="<b>𝙷𝙴𝚈 𝙸 𝙰𝙼 𝙾𝙿-𝚁𝙴𝙽𝙰𝙼𝙴 𝙱𝙾𝚃!</b>\n\n"
             "<b>𝙸 𝙲𝙰𝙽 𝚁𝙴𝙽𝙰𝙼𝙴 𝙼𝙴𝙳𝙸𝙰 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝚃!</b>\n"
             "<b>𝚂𝙿𝙴𝙴𝙳 𝙳𝙴𝙿𝙴𝙽𝙳𝚂 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙼𝙴𝙳𝙸𝙰 𝙳𝙲.</b>\n\n"
             "<b>𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙼𝙴𝙳𝙸𝙰 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝙸𝚃 𝚆𝙸𝚃𝙷 /rename 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.</b>",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("𝙱𝙾𝚃 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂",
                                      callback_data="showSettings")
        ]])
    )


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="<b>𝙸 𝙲𝙰𝙽 𝚁𝙴𝙽𝙰𝙼𝙴 𝙼𝙴𝙳𝙸𝙰 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝚃!</b>\n"
             "<b>𝚂𝙿𝙴𝙴𝙳 𝙳𝙴𝙿𝙴𝙽𝙳𝚂 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙼𝙴𝙳𝙸𝙰 𝙳𝙲.</b>\n\n"
             "<b>𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙼𝙴𝙳𝙸𝙰 𝙰𝙽𝙳 𝚁𝙴𝙿𝙻𝚈 𝙸𝚃 𝚆𝙸𝚃𝙷 /rename 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.</b>\n\n"
             "<b>𝚃𝙾 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙸𝙼𝙰𝙶𝙴 𝚆𝙸𝚃𝙷 /set_thumbnail</b>\n\n"
             "<b>𝚃𝙾 𝚂𝙴𝙴 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝙿𝚁𝙴𝚂𝚂 /show_thumbnail</b>",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("𝙱𝙾𝚃 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂",
                                      callback_data="showSettings")]])
    )
