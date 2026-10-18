# Telegram Virtual Coin Games — Railway Starter

This is a fresh implementation of virtual-coin games, not a full port of the uploaded legacy 800 KB bot source. The original file is not modified.

## Features
- Telegram bot commands: `/start`, `/balance`, `/games`, `/play <game> <stake>`, `/top`, `/transfer <amount>` as a reply to the recipient, `/duel <stake>` in a group, `/id`.
- Ten game choices and a Telegram Mini App page.
- SQLite virtual wallet, wins/losses, leaderboard, and two-player group duels with join/cancel buttons.
- Optional separate `selfbot.py` component for the owner's own Telegram account only.
- Environment-based secrets and Railway `Procfile`.

## Railway setup
1. Upload the files to a private GitHub repository.
2. Create a Railway project from that repository.
3. Add `BOT_TOKEN` in Railway Variables. Set `WEBAPP_URL` to the app's public HTTPS Railway domain and redeploy after the domain exists. Set `OWNER_ID` to your numeric Telegram user ID if you want owner-only duel cancellation.
4. Railway runs `python main.py`. The bot serves the Mini App and API on the provided `PORT`.
5. In BotFather, configure the Mini App/menu URL to the same public HTTPS URL if desired. The `/start` button appears when `WEBAPP_URL` is set to an HTTPS URL.

## Optional owner selfbot
`selfbot.py` is separate and is not launched by the default Procfile. It requires `PYROGRAM_API_ID`, `PYROGRAM_API_HASH`, and `PYROGRAM_SESSION` in private environment variables, for the owner's own account only. Run it as a separate Railway service with start command `python selfbot.py` only if you understand the account-security implications. Never share or commit a session string. This project does not collect login codes, 2FA passwords, phone numbers, or other users' session strings.

## Notes and limitations
- Coins are virtual and have no cash value or withdrawal feature.
- New users begin with 1,000 virtual coins. The economy uses a local SQLite file; configure a persistent Railway volume and set `DB_PATH` to its mounted path if balances must survive redeploys. Do not use multiple replicas against a local SQLite database.
- Mini App requests validate Telegram `initData` against the bot token.
- The Mini App currently supports play, balance, and leaderboard. Transfers and group duels are available through bot commands.
- The legacy source file has not been merged because it includes account-session handling and source-replacement capabilities that require a separate security review.
- Per request, no tests or live Telegram/Railway deployment checks were run. Configure secrets before starting; never place tokens in source files.
