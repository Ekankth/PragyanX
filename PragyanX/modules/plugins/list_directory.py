from . import *
from PragyanX.lib import *

@randydev(command("ls", cmd) & owner)
async def list_directories_cmd(c: Client, m: Message):
    await list_directories(c, m)
