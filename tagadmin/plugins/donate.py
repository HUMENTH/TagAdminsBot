from pyrogram import Client, filters
from pyrogram.types import Message
from tagadmin import COMMAND_HAND_LER, CONTACT_OWNER

# -- Constants -- #
DONATE_TEXT = """
Glad you'd like to donate!

You can donate my Owner by contacting him >>> @{} \
If you donate, the limit for download limit size \
of files would increase as he may upgrade the servers!
"""
# -- Constants End -- #


# Command for asking to donate owner
@Client.on_message(filters.command("donate", COMMAND_HAND_LER))
async def donate_owner(c: Client, m: Message):

    if m.chat.type in ("supergroup", "group"):

        try:
            await c.send_message(
                m.from_user.id, DONATE_TEXT.format(CONTACT_OWNER), parse_mode="markdown"
            )

            await m.reply_text(
                "**I've sent you message in your PM!**",
                parse_mode="markdown",
                reply_to_message_id=m.message_id,
            )
            return
        except:
            await message.reply_text(
                "**Contact me in PM first**",
                parse_mode="markdown",
                reply_to_message_id=m.message_id,
            )
            return

    await m.reply_text(
        DONATE_TEXT.format(CONTACT_OWNER),
        reply_to_message_id=m.message_id,
        parse_mode="markdown",
    )
    return
