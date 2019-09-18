from instabot import Bot
import sys
sys.path.append("/root/instabot/examples")

from creds import *

bot = Bot()
bot.login( username=username, password=password )

bot.upload_video( '/replace/with/path/to/video/file', caption='Replace with your caption')