import requests
import colorama

def main(shared_data):
    username = shared_data.get('username')
    output = shared_data.get('output')
    response = requests.get(f'https://xboxgamertag.com/search/{username}')
    if response.status_code == 200:
        print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} {username} was found : https://xboxgamertag.com/search/{username}")
        open(output, "a").write(f"https://xboxgamertag.com/search/{username}\n")
    else:
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.RESET} {username} was not found : https://xboxgamertag.com/search/{username}")