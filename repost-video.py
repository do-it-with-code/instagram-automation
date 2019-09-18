"""
    instabot example

    Workflow:
    1) Repost video to your account
"""

import os
import sys
from creds import *

url = sys.argv[1]
caption = sys.argv[2]

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot
from instabot.bot.bot_support import read_list_from_file


def exists_in_posted_medias(new_media_id, path='posted_medias.txt'):
    medias = read_list_from_file(path)
    return new_media_id in medias


def update_posted_medias(new_media_id, path='posted_medias.txt'):
    medias = read_list_from_file(path)
    medias.append(str(new_media_id))
    with open(path, 'w') as file:
        file.writelines('\n'.join(medias))
    return True


def repost_video(bot, new_media_id, caption, path='posted_medias.txt'):
    if exists_in_posted_medias(new_media_id, path):
        bot.logger.warning("Media {0} was uploaded earlier".format(new_media_id))
        return False
    video_path = bot.download_video( new_media_id )
    if not video_path:
        return False

    if bot.upload_video(video_path, caption=caption ):
        update_posted_medias(new_media_id, path)
        bot.logger.info('Media_id {0} is saved in {1}'.format(new_media_id, path))

def get_media_owner_username( bot, new_media_id  ):
    pk = bot.get_media_owner( new_media_id  )
    username = bot.get_user_info( pk )['username']
    return username

bot = Bot()
bot.login( username=username, password=password )
media_id = bot.get_media_id_from_link( url )
media_owner = get_media_owner_username( bot, media_id )
caption += "( via {} )".format( media_owner )
print( caption, media_id )

if not media_id:
    print('Media id is empty!')
    exit(1)

repost_video(bot, media_id, caption )