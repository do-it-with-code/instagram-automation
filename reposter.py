"""
    instabot example

    Workflow:
    1) Repost photo or video to your account
"""

import os
import sys
from creds import *
import json, requests, operator, random

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot
from instabot.bot.bot_support import read_list_from_file

# get top media by hashtag
tag = 'funnyvideo' # change to your hashtag
instaurl = 'https://www.instagram.com/explore/tags/{}/?__a=1'.format( tag )
r = requests.get( instaurl )
data = r.json()['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']
posts = {}
for i in data:
    shortcode = i['node']['shortcode']
    likes = i['node']['edge_liked_by']['count']
    posts[shortcode] = likes

sorted_d = sorted(posts.items(), key=operator.itemgetter(1), reverse=True )
print( sorted_d )
url = 'https://instagram.com/p/{}'.format ( list( sorted_d )[0][0] )
print( url )

def exists_in_posted_medias(new_media_id, path='posted_medias.txt'):
    medias = read_list_from_file(path)
    return new_media_id in medias

def update_posted_medias(new_media_id, path='posted_medias.txt'):
    medias = read_list_from_file(path)
    medias.append(str(new_media_id))
    with open(path, 'w') as file:
        file.writelines('\n'.join(medias))
    return True


def repost( bot, new_media_id, path='posted_medias.txt'):
    if exists_in_posted_medias(new_media_id, path):
        bot.logger.warning("Media {0} was uploaded earlier".format(new_media_id))
        return False

    media_type = bot.get_media_info( new_media_id )[0]['media_type']
    path = ''
    if media_type == 2:
       path = bot.download_video( new_media_id )
       if bot.upload_video( path, caption ):
          bot.logger.info('Media_id {0} is saved in {1}'.format(new_media_id, path))

    elif media_type == 1:
       path = bot.download_photo( new_media_id )
       if bot.upload_photo( path, caption ):
          bot.logger.info('Media_id {0} is saved in {1}'.format(new_media_id, path))

    if not path:
        return False

def get_media_id( bot, url ):
    media_id = bot.get_media_id_from_link( url )
    return media_id

def get_media_owner_username( bot, new_media_id  ):
    pk = bot.get_media_owner( new_media_id  )
    username = bot.get_user_info( pk )['username']
    return username

def get_hashtags_to_post( bot, tag ):
    bot.api.search_tags( tag )
    res = bot.api.last_json

    tags = []
    for i in res["results"]:
       tags.append( i['name'] )

    tags_to_post = random.sample( tags, 29 )
    tags_to_post = [ '#' + s  for s in tags_to_post ]
    tags_to_post = ' '.join( tags_to_post )
    return tags_to_post

bot = Bot()
bot.login( username=username, password=password )
media_id = get_media_id( bot, url )
username = get_media_owner_username( bot, media_id  )
use_tags = get_hashtags_to_post( bot, tag )
caption = 'your caption goes here #{} {} ( via {} )'.format( tag, use_tags, username ) # change 'your caption goes here'

print( caption )

if not media_id:
    print('Media id is empty!')
    exit(1)

repost( bot, media_id )