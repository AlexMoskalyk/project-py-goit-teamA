from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

# Словник для кольорів
COLORS = {
    'ERROR': Fore.RED,
    'SUCCESS': Fore.GREEN,
    'INPUT': Fore.BLUE
}

# Функція для виводу сповіщень
def print_message(message: str, color: str):
    print(f"{COLORS[color]}{message}{Style.RESET_ALL}")
