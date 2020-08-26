import time
from pyrogram import Client, filters
from pyrogram.types import Message
from tagadmin import COMMAND_HAND_LER
from tagadmin.utils.custom_filters import owner_filter


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & owner_filter)
async def ping(c: Client, m: Message):
    start = time.time()
    reply = await m.reply_text("Pinging...", reply_to_message_id=m.message_id)
    delta_ping = time.time() - start
    await reply.edit_text(
        f"**Pong!**\n`{delta_ping * 1000:.3f} ms`", parse_mode="markdown"
    )
    return
