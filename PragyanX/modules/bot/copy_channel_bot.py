

from PragyanX import app
from PragyanX.lib import *

@app.on_message(filters.private)
async def take_channel(client: Client, message: Message):
    await ass_copy_link(client, message)
