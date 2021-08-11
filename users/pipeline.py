from datetime import datetime

import requests
from django.conf import settings
from social_core.exceptions import AuthForbidden

from users.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = f'https://api.vk.com/method/users.get/?fields=bdate,sex,about,photo_max_orig&access_token={response["access_token"]}&v=5.92'
    response = requests.get(api_url)

    if response.status_code != 200:
        return
    data = response.json()['response'][0]

    if 'sex' in data:
        if data['sex'] == 1:
            user.userprofile.gender = UserProfile.FEMALE
        elif data['sex'] == 2:
            user.userprofile.gender = UserProfile.MALE

    if 'about' in data:
        user.userprofile.about_me = data['about']

    if 'bdate' in data:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y')
        age = datetime.now().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        user.age = age

    if 'photo_max_orig' in data:
        image_data = requests.get(data['photo_max_orig'])
        image = open(f'{settings.MEDIA_ROOT}/users_images/{user.username}.jpg', 'wb')
        image.write(image_data.content)
        image.close()
        user.image = f'/users_images/{user.username}.jpg'

    user.is_active = True
    user.save()
