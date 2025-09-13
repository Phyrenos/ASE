import requests
from urllib.parse import quote_plus
from json import dumps, decoder
import colorama


def main(shared_data):
    username = shared_data.get('username')
    output = shared_data.get('output')
    body = "signed_body=SIGNATURE." + quote_plus(
        dumps({"q": username, "skip_recovery": "1"}, separators=(",", ":"))
    )
    headers = {
        "Accept-Language": "en-US",
        "User-Agent": "Instagram 101.0.0.15.120",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-IG-App-ID": "124024574287414",
        "Accept-Encoding": "gzip, deflate",
        "Host": "i.instagram.com",
        "Connection": "keep-alive",
        "Content-Length": str(len(body))
    }   
    response = requests.post(
        'https://i.instagram.com/api/v1/users/lookup/',
        headers=headers,
        data=body
    )
    if response.json()['status'] != 'fail':
        print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} {username} was found : https://www.instagram.com/{username}/")
        open(output, "a").write(f"https://www.instagram.com/{username}/\n")
    else:
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.RESET} {username} was not found : https://www.instagram.com/{username}/")
    