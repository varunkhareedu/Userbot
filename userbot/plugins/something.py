''' Whatever Plugin by Noobs of Telegram i.e. @pureindialover '''

from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"hai"))
async def hai(event):
    if event.fwd_from:
        return
    await event.edit("🎲")
