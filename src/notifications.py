from colorama import Fore, Style, init

init(autoreset=True)

def print_message(message: str, message_type: str):
    if message_type == 'SUCCESS':
        print(Fore.GREEN + message)
    elif message_type == 'ERROR':
        print(Fore.RED + message)
    elif message_type == 'INPUT':
        print(Fore.BLUE + message)
    elif message_type == 'WARNING':
        print(Fore.YELLOW + message)
    elif message_type == 'HELP':
        print(Fore.MAGENTA + message)
    else:
        print(Fore.WHITE + message)