import os
from django.conf import settings
settings.configure()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import requests as rq
import time


public_key = 'NGMwMmMzNTVlYzQ3NDRmMjk1NjQ1ZDdhMTA2YmE4M2Q'
url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/BTCUSD'
headers = {'x-ba-key': public_key}
for i in range(60):
    time.sleep(1)
    response = rq.get(url=url, headers=headers)
    if response.status_code == 200:
        print(response.json()['ask'])












