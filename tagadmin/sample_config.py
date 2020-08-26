import os


class Config:
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    TMP_DIR = os.environ.get("TMP_DIR", "./TEMP/")
    CHANNEL = os.environ.get("CHANNEL", None)
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "/")
    CONTACT_OWNER = os.environ.get("CONTACT_OWNER", None)
    MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", None)
    ENV = os.environ.get("ENV", True)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
