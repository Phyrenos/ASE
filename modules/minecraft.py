import requests
import colorama

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'DNT': '1',
    'Sec-GPC': '1',
    'Priority': 'u=0, i',
}

def main(shared_data):
    username = shared_data.get('username')
    output = shared_data.get('output')
    response = requests.get(f'https://minecraftuuid.com/player/{username}', headers=headers)
    if 'No user was found matching that username or UUID.' not in response.text:
        print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} {username} was found : https://minecraftuuid.com/player/{username}")
        open(output, "a").write(f"https://minecraftuuid.com/player/{username}\n")
    else:
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.RESET} {username} was not found : https://minecraftuuid.com/player/{username}")
    