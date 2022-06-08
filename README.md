# Google Translate Bot for Discord 🗣

This is a custom Google Translate Discord bot using the [**googletrans**](https://pypi.org/project/translate/3.1.0/) API library 

## Install Directly on Local Computer

- Create a [Bot account](https://discordpy.readthedocs.io/en/stable/discord.html) and invite the Bot to a Discord server

- Add `translate_discord.py` and `keep_alive.py` to a new repository on [Replit](https://replit.com/)

- Replace `TOKEN` with the Discord Bot token

### Replit

Run the following in the bash shell:

`pip install discord`

`pip install translate==3.1.0`

`pip install Flask`

- Then run `main.py`, this should generate a URL `https://googletranslatebot.winniiew.repl.co/` that can then be used in [UptimeRobot](https://uptimerobot.com/) to host the Discord bot.

<p align="center">
<img width="667" alt="help2" src="https://user-images.githubusercontent.com/86391366/172135241-7c6a87ca-745d-4f71-b87c-f87895cdaf39.png">
<p>

### Uptime Robot
  
1. Click `+ Add New Monitor`
2. Select `HTTP(s)` under `Monitor Types`
3. Paste the generated URL
4. Change the monitoring interval to 5 minutes

 <p align="center">
<img width="667" alt="help" src="https://user-images.githubusercontent.com/86391366/172134366-52674385-f150-4f1c-aa58-d6da24731c40.PNG">
<p>
  
## Invite Bot to join server
https://discord.com/api/oauth2/authorize?client_id=983219732712931339&permissions=257698506816&scope=bot

### Commands 
The list of available languages within the [**googletrans library**](https://py-googletrans.readthedocs.io/en/latest/)

```
!t zh-tw hello

hello -> 你好 
```
  
```
!t en こんにちは
  
こんにちは -> hello
```

