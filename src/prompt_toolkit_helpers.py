from prompt_toolkit.completion import WordCompleter

# Список ключових слів для автозаповнення
keywords = [
    'add contact', 'show contacts', 'find contact', 'delete contact',
    'edit contact email', 'edit contact phone', 'delete contact phone',
    'contacts birthdays', 'add note', 'show notes', 'find note',
    'edit note', 'delete note', 'sort notes', 'cancel','help', 'exit','edit contact birthday','edit contact address'
]
completer = WordCompleter(keywords, ignore_case=True)