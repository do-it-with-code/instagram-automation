"""
    instabot example

    Workflow:
        Like last images with hashtag.
"""

import os
import sys
from creds import *

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

bot = Bot()
bot.login( username=username, password=password )

tags = [ 'funny', 'funnyvideos', 'funnymemes' ]
for i in tags:
 bot.like_hashtag( i, amount=50 )