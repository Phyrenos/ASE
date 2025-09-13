import requests
import colorama

# not valid 308 -> 404
# valid 308 -> 200
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Alt-Used': 'www.snapchat.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}
def main(shared_data):
    username = shared_data.get('username')
    output = shared_data.get('output')
    response = requests.get(f'https://www.snapchat.com/add/{username}', headers=headers, allow_redirects=True)
    if response.status_code == 200:
        print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} {username} was found : {response.url}")
        open(output, "a").write(f"{response.url}\n")
    else:
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.RESET} {username} was not found : https://www.snapchat.com/@{username}")
    