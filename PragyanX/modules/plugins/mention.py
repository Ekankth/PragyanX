from PragyanX import *
from PragyanX.lib import *

@randydev(command("tagpremium", cmd) & owner)
async def user_premium_fixed(c: Client, m: Message):
    await user_premium(c, m)
