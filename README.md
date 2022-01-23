# discord-twitch-clip-bot
Simple discord bot that takes twitch clip links and sends back the video in embed (useful for archiving of risky twitch clips or for sharing)

Issues:
- Does not use any form of regex, so it can only work with messages that only include the twitch link
- Does not send any error back if the file is too large to send (I could honestly probably make this, but I'm lazy)

Important notes:
- The twitch-dl.pyz included is from https://github.com/ihabunek/twitch-dl, if you want to verify it you can delete it and just redownload it from their release page, I just added it for simplicity
- Requires official discord.py, to get this just do "pip install discord"
