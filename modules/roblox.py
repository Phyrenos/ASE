import requests
import colorama


def main(shared_data):
    username = shared_data.get('username')
    output = shared_data.get('output')
    
    params = {
        'username': username,
    }
    response = requests.get('https://www.roblox.com/users/profile', params=params)
    if response.status_code == 200:
        print(f"{colorama.Fore.GREEN}[+]{colorama.Fore.RESET} {username} was found : https://www.roblox.com/user.aspx?username={username}")
        open(output, "a").write(f"https://www.roblox.com/user.aspx?username={username}\n")
    else:
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.RESET} {username} was not found : https://www.roblox.com/user.aspx?username={username}")
    