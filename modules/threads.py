import requests
import colorama

def main(shared_data):
    username = shared_data.get('username')
    output = shared_data.get('output')
    response = requests.get(f'https://www.threads.com/@{username}')
    if 'Threads • Log in' not in response.text:
        print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} {username} was found : https://www.threads.com/@{username}")
        open(output, "a").write(f"https://www.threads.com/@{username}\n")
    else:
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.RESET} {username} was not found : https://www.threads.com/@{username}")
