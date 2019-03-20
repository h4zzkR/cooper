import string
import random
from PIL import Image
from django.conf import settings
import pandas as pd
import uuid
import os
import datetime
import os
import datetime
#300s

def avatar_generator(size=10, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def image_preproc(img):
    image = Image.open(img)
    height, width = image.size
    left = (width - 110) / 2
    top = (height - 110) / 2
    right = (width + 110) / 2
    bottom = (height + 110) / 2
    image = image.crop((left, top, right, bottom))
    with open(settings.MEDIA_ROOT + '/tmp.png', 'wb') as out:
        image.save(out, 'PNG')


def token_generator(user):
    path = '../cooper/data'
    if 'user_tokens.csv' not in os.listdir(path):
        u_tokens = pd.DataFrame({
            'user' : user.nickname,
            'token' : uuid.uuid4().hex,
            'time' : datetime.datetime.now().time()
                         }, index=[0])
        u_tokens.to_csv(path + '/user_tokens.csv', index=False)
    else:
        u_tokens = pd.read_csv(path + '/user_tokens.csv')
        if user.nickname not in u_tokens['user'].values:
            idx = len(u_tokens)
            u_tokens.loc[idx] = {'user': user.nickname, 'token' : uuid.uuid4().hex,
                                 'time': datetime.datetime.now().time()}
        else:
            u_tokens['token'][u_tokens.user == user.nickname] = uuid.uuid4().hex
            u_tokens['time'][u_tokens.user == user.nickname] = datetime.datetime.now().time()
        u_tokens.to_csv(path + '/user_tokens.csv', index=False)
    return u_tokens[u_tokens.user == user.nickname]

def delete_on_reset(user):
    path = '../cooper/data'
    u_tokens = pd.read_csv(path + '/user_tokens.csv')
    u_tokens = u_tokens.drop(u_tokens[u_tokens.user == user.nickname].index)

def get_user_by_token(token):
    path = '../cooper/data'
    u_tokens = pd.read_csv(path + '/user_tokens.csv')
    return u_tokens[u_tokens.token == token]


