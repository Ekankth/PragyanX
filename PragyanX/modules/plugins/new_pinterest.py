from PragyanX import *
from PragyanX.lib import *

@randydev(command(["pintr", "pinterest"], cmd) & owner)
async def pinterest_handler(client: Client, message: Message):
    await pinterest_downloader(client, message)
