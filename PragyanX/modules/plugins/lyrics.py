from PragyanX import *
from PragyanX.lib import *

@randydev(command("lyrics", cmd) & owner)
async def lyrics_command(client: Client, message: Message):
    await lyrics(client, message)
