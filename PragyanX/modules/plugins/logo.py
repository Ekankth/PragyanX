from PragyanX import *
from PragyanX.lib import *


@randydev(command("logo", cmd) & owner)
async def logo_command(client: Client, message: Message):
    await logo_write(client, message)
