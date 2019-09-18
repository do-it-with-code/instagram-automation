from instabot import Bot
import sys

# replace the path with the location of your creds.py file 
sys.path.append("/root/instabot/examples")

from creds import *

bot = Bot()
bot.login( username=username, password=password )

bot.upload_photo( '/replace/with/path/to/image', caption='Replace with your caption and some hashtags')