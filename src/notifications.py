from colorama import Fore, Style, init

init(autoreset=True)

def print_message(message: str, message_type: str, end: str = '\n'):
    if message_type == 'SUCCESS':
        print(Fore.GREEN + message, end=end)
    elif message_type == 'ERROR':
        print(Fore.RED + message, end=end)
    elif message_type == 'INPUT':
        print(Fore.BLUE + message, end=end)
    elif message_type == 'WARNING':
        print(Fore.YELLOW + message, end=end)
    elif message_type == 'HELP':
        print(Fore.MAGENTA + message, end=end)
    else:
        print(Fore.WHITE + message, end=end)
    return ''