# Auto-Delete
A Simple Telegram Bot To Delete Group Messages After Specific Time.

## Deploy on Heroku
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
- DON'T FORGET TO TURN ON DYNOS

## Deploy in your VPS
```sh
git clone https://github.com/Arun-TG/AutoDelete/tree/Bot-Only
cd AutoDelete
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 sam.py
```


### Variables:
1. `API_ID` : Get From [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `ADMINS` : ID of Admins (Bot will not delete Messages of Admins)
4. `BOT_TOKEN` : Your Telegram Bot Token from [@BotFather](https://t.me/BotFather)
5. `BOT_USERNAME` : Your Bot Username Without '@'
6. `TIME` : Time Duration for deletion

##
- In [Bot-Only](https://github.com/Arun-TG/AutoDelete/tree/Bot-Only) Branch Bot can only delete message of Users.
- If you want to delete Messages Sent By Bots Deploy [Main](https://github.com/Arun-TG/AutoDelete/tree/main) Branch 

# Credits
- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Abir Hasan](https://github.com/AbirHasan2005)
- [SUBIN](https://github.com/subinps)
- [Me](https://t.me/Arun_TG)

* Inspiration➔ [Ten Seconds Delete](https://t.me/TenSecBot)
