from src.notifications import print_message

def input_error(func):
    """Декоратор для обробки помилок вводу."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError) as e:
            print_message(str(e), 'ERROR')
    return wrapper

def check_cancel(input_text: str):
    """Перевіряє, чи ввів користувач команду скасування."""
    if input_text.strip().lower() == "cancel":
        raise KeyboardInterrupt("Операція була скасована.")