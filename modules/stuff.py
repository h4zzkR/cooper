import string
import random
from PIL import Image
from django.conf import settings
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


def token_generator():
    return uuid.uuid4().hex

