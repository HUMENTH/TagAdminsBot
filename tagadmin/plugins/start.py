from pyrogram import Client, filters
from pyrogram.types import Message
from tagadmin import COMMAND_HAND_LER

# -- Constants -- #
START_TEXT = """
Hey {}

I'm @{}, a simple bot to Tag All Admins in a \
group easily by typing @admin or @admins

/help - Show help message
❤️ Source Code - [Github](https://github.com/Skuzzers/TagAdminsBot)

__**Made with ❤️ in India**__
"""

HELP_TEXT = f"""
{COMMAND_HAND_LER}start - Show Start message.
{COMMAND_HAND_LER}help - Check this help message.
{COMMAND_HAND_LER}donate - Get information about donating my owner.
@admin / @admins - Tag All the admins
"""
# -- Constants End -- #


@Client.on_message(filters.command("help", COMMAND_HAND_LER))
async def help_bot(c: Client, m: Message):

    await m.reply_text(
        HELP_TEXT, parse_mode="markdown", reply_to_message_id=m.message_id
    )
    return


@Client.on_message(filters.command("start", COMMAND_HAND_LER))
async def start_bot(c: Client, m: Message):

    user = m.from_user.first_name
    bot = await c.get_me()

    await m.reply_text(
        START_TEXT.format(user, bot.username),
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id,
        parse_mode="markdown",
    )
    return
