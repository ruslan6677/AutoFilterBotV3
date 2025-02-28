import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from LuciferMoringstar_Robot import Media
from Config import SESSION, API_ID, API_HASH, BOT_TOKEN
import pyromod.listen

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name=SESSION,
            api_id=10300036,
            api_hash=79c295e05c970ddd724f0762ba275104,
            bot_token=5482727166:AAGHP_ovslWbAOLMCSepqO0Si5QGyYfel7I,
            workers=50,
            plugins={"root": "LuciferMoringstar_Robot"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        self.username = '@' + me.username
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = Bot()
app.run()
