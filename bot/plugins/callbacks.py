# (c) @Aadhi000

from pyrogram import types
from bot.client import Client
from bot.core.db.database import db
from bot.core.file_info import (
    get_media_file_name,
    get_media_file_size,
    get_file_type,
    get_file_attr
)
from bot.core.display import humanbytes
from bot.core.handlers.settings import show_settings


@Client.on_callback_query()
async def cb_handlers(c: Client, cb: "types.CallbackQuery"):
    if cb.data == "showSettings":
        await cb.answer()
        await show_settings(cb.message)
    elif cb.data == "showThumbnail":
        thumbnail = await db.get_thumbnail(cb.from_user.id)
        if not thumbnail:
            await cb.answer("𝚈𝙾𝚄 𝙳𝙸𝙳𝙽'𝚃 𝚂𝙴𝚃 𝙰𝙽𝚈 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻!", show_alert=True)
        else:
            await cb.answer()
            await c.send_photo(cb.message.chat.id, thumbnail, "𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻",
                               reply_markup=types.InlineKeyboardMarkup([[
                                   types.InlineKeyboardButton("𝙳𝙴𝙻𝙴𝚃𝙴 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻",
                                                              callback_data="deleteThumbnail")
                               ]]))
    elif cb.data == "deleteThumbnail":
        await db.set_thumbnail(cb.from_user.id, None)
        await cb.answer("𝙾𝙺𝙰𝚈, 𝙸 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝚈𝙾𝚄𝚁 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻. 𝙽𝙾𝚆 𝙸 𝚆𝙸𝙻𝙻 𝙰𝙿𝙿𝙻𝚈 𝙳𝙴𝙵𝙰𝚄𝙻𝚃 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻.", show_alert=True)
        await cb.message.delete(True)
    elif cb.data == "setThumbnail":
        await cb.answer()
        await cb.message.edit("𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰𝙽𝚈 𝙿𝙷𝙾𝚃𝙾 𝚃𝙾 𝚂𝙴𝚃 𝚃𝙷𝙰𝚃 𝙰𝚂 𝙲𝚄𝚂𝚃𝙾𝙼 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻.\n\n"
                              "𝙿𝚁𝙴𝚂𝚂 /cancel 𝚃𝙾 𝙲𝙰𝙽𝙲𝙴𝙻 𝙿𝚁𝙾𝙲𝙴𝚂𝚂..")
        from_user_thumb: "types.Message" = await c.listen(cb.message.chat.id)
        if not from_user_thumb.photo:
            await cb.message.edit("<b>𝙿𝚁𝙾𝙲𝙴𝚂𝚂 𝙲𝙰𝙽𝙲𝙴𝙻𝙻𝙴𝙳</b>")
            return await from_user_thumb.continue_propagation()
        else:
            await db.set_thumbnail(cb.from_user.id, from_user_thumb.photo.file_id)
            await cb.message.edit("𝙾𝙺𝙰𝚈!\n"
                                  "𝙽𝙾𝚆 𝙸 𝚆𝙸𝙻𝙻 𝙰𝙿𝙿𝙻𝚈 𝚃𝙷𝙸𝚂 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻 𝚃𝙾 𝙽𝙴𝚇𝚃 𝚄𝙿𝙻𝙾𝙰𝙳𝚂.",
                                  reply_markup=types.InlineKeyboardMarkup(
                                      [[types.InlineKeyboardButton("𝙱𝙾𝚃 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂",
                                                                   callback_data="showSettings")]]
                                  ))
    elif cb.data == "setCustomCaption":
        await cb.answer()
        await cb.message.edit("Okay,\n"
                              "𝚂𝙴𝙽𝙳 𝙼𝙴 𝚈𝙾𝚄𝚁 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽.\n\n"
                              "𝙿𝚁𝙴𝚂𝚂 /cancel 𝚃𝙾 𝙲𝙰𝙽𝙲𝙴𝙻 𝙿𝚁𝙾𝙲𝙴𝚂𝚂..")
        user_input_msg: "types.Message" = await c.listen(cb.message.chat.id)
        if not user_input_msg.text:
            await cb.message.edit("<b>𝙿𝚁𝙾𝙲𝙴𝚂𝚂 𝙲𝙰𝙽𝙲𝙴𝙻𝙻𝙴𝙳</b>")
            return await user_input_msg.continue_propagation()
        if user_input_msg.text and user_input_msg.text.startswith("/"):
            await cb.message.edit("<b>𝙿𝚁𝙾𝙲𝙴𝚂𝚂 𝙲𝙰𝙽𝙲𝙴𝙻𝙻𝙴𝙳</b>")
            return await user_input_msg.continue_propagation()
        await db.set_caption(cb.from_user.id, user_input_msg.text.markdown)
        await cb.message.edit("𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝙰𝙳𝙳𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈!",
                              reply_markup=types.InlineKeyboardMarkup(
                                  [[types.InlineKeyboardButton("𝙱𝙾𝚃 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂",
                                                               callback_data="showSettings")]]
                              ))
    elif cb.data == "triggerApplyCaption":
        await cb.answer()
        apply_caption = await db.get_apply_caption(cb.from_user.id)
        if not apply_caption:
            await db.set_apply_caption(cb.from_user.id, True)
        else:
            await db.set_apply_caption(cb.from_user.id, False)
        await show_settings(cb.message)
    elif cb.data == "triggerApplyDefaultCaption":
        await db.set_caption(cb.from_user.id, None)
        await cb.answer("𝙾𝙺𝙰𝚈, 𝙽𝙾𝚆 𝙸 𝚆𝙸𝙻𝙻 𝙺𝙴𝙴𝙿 𝙳𝙴𝙵𝙰𝚄𝙻𝚃 𝙲𝙰𝙿𝚃𝙸𝙾𝙽.", show_alert=True)
        await show_settings(cb.message)
    elif cb.data == "showCaption":
        caption = await db.get_caption(cb.from_user.id)
        if not caption:
            await cb.answer("𝚈𝙾𝚄 𝙳𝙸𝙳𝙽'𝚃 𝚂𝙴𝚃 𝙰𝙽𝚈 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽!", show_alert=True)
        else:
            await cb.answer()
            await cb.message.edit(
                text=caption,
                parse_mode="Markdown",
                reply_markup=types.InlineKeyboardMarkup([[
                    types.InlineKeyboardButton("𝙱𝙰𝙲𝙺", callback_data="showSettings")
                ]])
            )
    elif cb.data == "triggerUploadMode":
        await cb.answer()
        upload_as_doc = await db.get_upload_as_doc(cb.from_user.id)
        if upload_as_doc:
            await db.set_upload_as_doc(cb.from_user.id, False)
        else:
            await db.set_upload_as_doc(cb.from_user.id, True)
        await show_settings(cb.message)
    elif cb.data == "showFileInfo":
        replied_m = cb.message.reply_to_message
        _file_name = get_media_file_name(replied_m)
        text = f"**𝙵𝙸𝙻𝙴 𝙽𝙰𝙼𝙴 :** `{_file_name}`\n\n" \
               f"**𝙵𝙸𝙻𝙴 𝙴𝚇𝚃𝙴𝙽𝚂𝙸𝙾𝙽 :** `{_file_name.rsplit('.', 1)[-1].upper()}`\n\n" \
               f"**𝙵𝙸𝙻𝙴 𝚃𝚈𝙿𝙴 :** `{get_file_type(replied_m).upper()}`\n\n" \
               f"**𝙵𝙸𝙻𝙴 𝚂𝙸𝚉𝙴 :** `{humanbytes(get_media_file_size(replied_m))}`\n\n" \
               f"**𝙵𝙸𝙻𝙴 𝙵𝙾𝚁𝙼𝙰𝚃 :** `{get_file_attr(replied_m).mime_type}`"
        await cb.message.edit(
            text=text,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=types.InlineKeyboardMarkup(
                [[types.InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data="closeMessage")]]
            )
        )
    elif cb.data == "closeMessage":
        await cb.message.delete(True)
