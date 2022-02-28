import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

import pandas as pd

f = open("./../env/upbit.txt")
lines = f.readlines()
access_key = lines[0].strip()
secret_key = lines[1].strip()
telegram_bot_token = lines[2].strip()
telegram_user = lines[3].strip()
f.close()

#print(access_key + " : " + secret_key + " : " + telegram_bot_token + " : " + telegram_user)

server_url = "https://api.upbit.com/"

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)
#print(res.json())

잔고리스트 = pd.DataFrame(res.json(),columns=['currency','balance','locked','avg_buy_price'])
print(잔고리스트)

