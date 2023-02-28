#Edited By LAPSCA TEAM 2023© 

import os

import logging

logging.basicConfig(

    format='%(name)s - %(levelname)s - %(message)s',

    handlers=[logging.FileHandler('log.txt'),

              logging.StreamHandler()],

    level=logging.INFO

)

class Config(object):

    WEBHOOK = os.environ.get("BOT_TOKEN", False)

    BOT_TOKEN = os.environ.get("BOT_TOKEN",6096638469:AAEqCw5n3rAxFpd28Uf0MkZ8vpgVBgBjonY "")

    API_ID = int(os.environ.get("API_ID", 26109769))

    API_HASH = os.environ.get("3f3b6ea94785f21bf50f5724977fb41f")

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "noshey25@hotmail.com")

    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "xnoshyx1998")

    TG_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 2024))

    HTTP_PROXY = os.environ.get("HTTP_PROXY",103.122.168.226:8080 "")

    PROCESS_MAX_TIMEOUT = 3700

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))

    OWNER_ID = int(os.environ.get("OWNER_ID", "1891604652"))

    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@uplovdBot")

    ADL_BOT_RQ = {3700}

    AUTH_USERS = list({int(x)

                      for x in os.environ.get("AUTH_USERS", "0").split()})

    AUTH_USERS.append(OWNER_ID)
