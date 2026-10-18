"""Optional Pyrogram userbot for the owner's own Telegram account only.

Run separately from bot.py with PYROGRAM_API_ID, PYROGRAM_API_HASH, and
PYROGRAM_SESSION supplied as private Railway variables. Never commit session
strings or share them. This module does not ask for or collect login codes,
2FA passwords, phone numbers, or other users' sessions.
"""
import asyncio, logging, os
from pyrogram import Client, filters

logging.basicConfig(level=logging.INFO)
log=logging.getLogger('owner-selfbot')
API_ID=os.getenv('PYROGRAM_API_ID','').strip()
API_HASH=os.getenv('PYROGRAM_API_HASH','').strip()
SESSION=os.getenv('PYROGRAM_SESSION','').strip()

async def main():
    if not API_ID.isdigit() or not API_HASH or not SESSION:
        raise RuntimeError('Set PYROGRAM_API_ID, PYROGRAM_API_HASH and PYROGRAM_SESSION as private environment variables. This is for the owner account only.')
    app=Client('owner_userbot', api_id=int(API_ID), api_hash=API_HASH, session_string=SESSION, in_memory=True)
    @app.on_message(filters.me & filters.command('selfstatus', prefixes='/'))
    async def selfstatus(client, message):
        await message.reply_text('✅ Userbot فعال است. این ابزار فقط برای حساب مالک پیکربندی شده است.')
    await app.start()
    log.info('Owner userbot is running.')
    await asyncio.Event().wait()

if __name__=='__main__': asyncio.run(main())
