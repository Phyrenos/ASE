import requests
import colorama


def main(shared_data):
    username = shared_data.get('username')
    output = shared_data.get('output')

    response = requests.get(f'https://www.facebook.com/{username}')
    if "This content isn't available at the moment" not in response.text:
        print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} {username} was found : https://www.facebook.com/{username}")
        open(output, "a").write(f"https://www.facebook.com/{username}\n")
    else:
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.RESET} {username} was not found : https://www.facebook.com/{username}")
    
    