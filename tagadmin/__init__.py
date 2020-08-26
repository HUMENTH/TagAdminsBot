import os
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if bool(os.environ.get("ENV", False)):
    from tagadmin.sample_config import Config
else:
    from tagadmin.config import Development as Config


LOGGER = logging.getLogger(__name__)
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
OWNER_ID = Config.OWNER_ID
TMP_DIR = Config.TMP_DIR
CHANNEL = Config.CHANNEL
COMMAND_HAND_LER = Config.COMMAND_HAND_LER
CONTACT_OWNER = Config.CONTACT_OWNER
MESSAGE_DUMP = Config.MESSAGE_DUMP

if not os.path.isdir(TMP_DIR):
    os.makedirs(TMP_DIR)
