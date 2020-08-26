from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from tagadmin import APP_ID, API_HASH, LOGGER, TG_BOT_TOKEN, TMP_DIR, MESSAGE_DUMP


class TagAdmin(Client):
    """Start bot using a Class TagAdmin, it will start the bot with TagAdmin().run()
    Takes values from sample_config.py or config.py file"""

    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            name,
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DIR,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            workers=8,
        )

    async def start(self):
        await super().start()

        me = await self.get_me()
        # Show message in LOGGER when bot starts
        LOGGER.info(
            f"TagAdminsBot based on Pyrogram v{__version__}\n"
            f"(Layer {layer}) started on @{me.username}"
        )

        # Send message to MESSAGE_DUMP when bot starts
        await self.send_message(MESSAGE_DUMP, "<b><i>Bot Started</i></b>")

    async def stop(self, *args):
        await super().stop()
        # Show message in LOGGER when bot stops
        LOGGER.info("TagAdminsBot stopped!\nkthxbye...!")


if __name__ == "__main__":
    TagAdmin().run()
