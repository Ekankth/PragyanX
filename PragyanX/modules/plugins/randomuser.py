from PragyanX import *
from PragyanX.lib import *

@randydev(command("randomuser", cmd) & owner)
async def randomuser_handler(client: Client, message: Message):
    await randomuser(client, message)
