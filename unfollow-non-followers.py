"""
    instabot example

    Workflow:
        1) unfollows users that don't follow you.
"""

import argparse
import os
import sys
from creds import *

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

bot = Bot()
bot.login( username=username, password=password )
bot.unfollow_non_followers( n_to_unfollows=50 )