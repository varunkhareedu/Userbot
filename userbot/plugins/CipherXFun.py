# Original written by @Hackintush
"""Available Commands:
.gam"""

@borg.on(admin_cmd(pattern="gam"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("")
