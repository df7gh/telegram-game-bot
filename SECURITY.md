# Security

- Never commit `BOT_TOKEN`, `PYROGRAM_SESSION`, API credentials, or `.env` values.
- Keep the repository private while configuring it and rotate any token that was exposed.
- The optional selfbot is intended only for the repository owner's own Telegram account. Do not collect or store other people's login codes, passwords, or session strings.
- The default bot is a virtual-coin game only. It has no deposits, cash-out, or real-money transfers.
- SQLite on an ephemeral filesystem may be lost during redeploy; use a private persistent volume for production balances.
