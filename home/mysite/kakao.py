import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'b7ce8cbd8b718020aef605de3e812865'
redirect_uri = 'https://example.com/oauth'
authorize_code = '1vzFAeUIdiec0zoF8AXGxFeo39nGJ_Y0HU3Ff1b5NwRMOFGivd5lbTTl6cbSIzK81Asj6wo9dNoAAAGC2Av2ag'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)