#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Harshil H P | Modifieded By : @Harshil8981

import os
from config import Config
from pyrogram import Client as Harshil

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = Harshil("@UPLOADER_HP_BOT",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    Warrior.run()
