import requests
import time
import json
from bs4 import BeautifulSoup

def get_response(url, method='GET'):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "cookie":"__cfduid=da350b8e01521848041e557b8840722281595350016; PHPSESSID=rgr9ath2l0aumnkbt9s4k41if4"
    }
    response = requests.get(url, headers=headers)
	#response = requests.request(method, url, headers=headers, timeout=15)
    text_response = response.text
    return text_response


while True:
    res = get_response("https://faucetbch.com/index.php?a=faucet2")
    text_response = res
    parse_data = BeautifulSoup(res, features="lxml")
    out = parse_data.find('button',{'class':'bet'})
    if "Max claims reached for today! Claim again in 24 hours. Deposit BCH to earn much more." in text_response:
        print('Max claims lets wait for a day')
        time.sleep(86400)
        continue
    if out is not None:
        print('Logged out')
        res = get_response("https://faucetbch.com/index.php?login=true&email=qqxfgklk4el69e5u45wphqm245k3t5rhpcwac7uhwe")
        res = get_response("https://faucetbch.com/index.php?a=faucet2")
        print(res)
        time.sleep(182)
    else:
        print ('Logged in')
        print(res)
        time.sleep(182)