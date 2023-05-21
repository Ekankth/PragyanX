from PragyanX import *
from PragyanX.lib import *

@randydev(command("animequote", cmd) & owner)
async def animechan_hanlder(client: Client, message: Message):
    await api_animechan_new(client, message)
