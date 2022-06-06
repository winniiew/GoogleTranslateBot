This is a custom Google Translate Discord bot

Follow the instructions: https://discordpy.readthedocs.io/en/stable/discord.html to create a Bot account and invite the Bot to a Discord server

Add `translate_discord.py` and `keep_alive.py` to a new repository on https://replit.com/

Replit:

Run in the shell:

`pip install discord`

`pip install googletrans==3.1.0a0`

Then run `main.py`, this should generate a URL `https://googletranslatebot.winniiew.repl.co/` that can then be used in https://uptimerobot.com/ to host the Discord bot.


<img width="667" alt="help2" src="https://user-images.githubusercontent.com/86391366/172135241-7c6a87ca-745d-4f71-b87c-f87895cdaf39.png">


Uptime Robot:
1. Click `+ Add New Monitor`
2. Select `HTTP(s)` under `Monitor Types`
3. Paste the generated URL
4. Change the monitoring interval to 5 minutes

<img width="467" alt="help" src="https://user-images.githubusercontent.com/86391366/172134366-52674385-f150-4f1c-aa58-d6da24731c40.PNG">
