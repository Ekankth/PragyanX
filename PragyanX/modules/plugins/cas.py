from . import *
from PragyanX.lib import *


@randydev(command("cas", cmd) & owner)
async def cas_command(c: Client, m: Message):
    await cas_check(c, m)
