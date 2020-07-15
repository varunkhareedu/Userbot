''' Whatever Plugin by Noobs of Telegram i.e. @pureindialover '''

from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"color"))
async def color (event):
    if event.fwd_from:
        return
    await event.edit("<div><span style="color:#ff0000;">!<//nspan><span style="color:#ff7f00;">Y<//nspan><span style="color:#ffbf00;">o<//nspan><span style="color:#ffff00;">u<//nspan><span style="color:#00ff00;"> <//nspan><span style="color:#00ff80;">c<//nspan><span style="color:#00ffff;">a<//nspan><span style="color:#0000ff;">n<//nspan></div>")

