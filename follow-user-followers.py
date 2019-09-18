"""
    instabot example

    Workflow:
        Follow user's followers by username.
"""
import os
import sys
from creds import *

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

bot = Bot()
bot.login(username=username, password=password)

bot.follow_followers( 'funnymike' , nfollows=50 )