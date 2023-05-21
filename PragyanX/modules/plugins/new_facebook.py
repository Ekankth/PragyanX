from PragyanX import *
from PragyanX.lib import *

@randydev(command("fbdl", cmd) & owner)
async def facebook_handler(client: Client, message: Message):
    await facebook_downloader(client, message)
