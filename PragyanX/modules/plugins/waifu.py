from PragyanX import *
from PragyanX.lib import *

@randydev(command("waifu", cmd) & owner)
async def waifu_hanlder(client: Client, message: Message):
    await api_waifu_main(client, message)
