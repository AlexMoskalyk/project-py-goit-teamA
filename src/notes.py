import pickle
from typing import List
from src.notifications import print_message
from src.contacts_book import Field

class Title(Field):
    """Клас для заголовку нотатки (обмеження до 50 символів)."""
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Title cannot be empty or just whitespace.")
        if len(value.strip()) > 50:
            raise ValueError("Title cannot exceed 50 characters.")
        super().__init__(value.strip())

class Note:
    """Клас для нотатки."""
    def __init__(self, title: Title, text: str, tags: List[str] = []):
        self.title = title
        self.text = text
        self.tags = tags

    def __str__(self) -> str:
        return f"{self.title.value} - {self.text} - Tags: {', '.join(self.tags)}"

class NoteBook:
    """Клас для управління нотатками."""
    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self, note: Note):
        """Додає нотатку."""
        if self.note_exists(note.title.value):
            print_message("Note with this title already exists.", 'ERROR')
            return
        self.notes.append(note)
        print_message("Note successfully added.", 'SUCCESS')

    def search_notes(self, query: str) -> List[Note]:
        """Шукає нотатки за запитом."""
        results = [n for n in self.notes if query.lower() in n.title.value.lower() or any(query.lower() in tag.lower() for tag in n.tags)]
        if not results:
            print_message("No notes found.", 'ERROR')
        return results

    def sort_notes_by_tag(self, tag: str) -> List[Note]:
        """Сортує нотатки за тегом."""
        return sorted([n for n in self.notes if tag.lower() in (t.lower() for t in n.tags)], key=lambda x: x.title.value)

    def remove_note(self, title: str):
        """Видаляє нотатку за заголовком."""
        initial_length = len(self.notes)
        self.notes = [n for n in self.notes if n.title.value.lower() != title.lower()]
        if len(self.notes) < initial_length:
            print_message("Note successfully removed.", 'SUCCESS')
        else:
            print_message("Note not found.", 'ERROR')

    def edit_note(self, old_title: str, new_title: Title, new_text: str, new_tags: List[str]):
        """Редагує нотатку."""
        for note in self.notes:
            if note.title.value.lower() == old_title:
                note.title = new_title
                note.text = new_text
                note.tags = new_tags
                print_message("Note successfully edited.", 'SUCCESS')
                return
        print_message("Note not found.", 'ERROR')

    def save_notes(self, filename: str = 'notes.pkl', show_message: bool = True):
        """Зберігає нотатки у файл."""
        if not self.notes:
            if show_message:
                print_message("No notes to save.", 'ERROR')
            return
        with open(filename, 'wb') as file:
            pickle.dump(self.notes, file)
        if show_message:
            print_message("Notes successfully saved.", 'SUCCESS')

    def load_notes(self, filename: str = 'notes.pkl', show_message: bool = True):
        """Завантажує нотатки з файлу."""
        try:
            with open(filename, 'rb') as file:
                self.notes = pickle.load(file)
            if show_message:
                print_message("Notes successfully loaded.", 'SUCCESS')
        except FileNotFoundError:
            self.notes = []
            if show_message:
                print_message(f"File {filename} not found. Initializing empty notes.", 'ERROR')
        except Exception as e:
            self.notes = []
            if show_message:
                print_message(f"An error occurred while loading notes: {str(e)}", 'ERROR')

    def display_notes(self):
        """Відображає всі нотатки."""
        if not self.notes:
            print_message("No notes to display.", 'ERROR')
        else:
            for note in self.notes:
                print_message(str(note), 'SUCCESS')

    def note_exists(self, title: str) -> bool:
        """Перевіряє, чи існує нотатка з таким заголовком."""
        for note in self.notes:
            if note.title.value.lower() == title.lower():
                return True
        return False

    def display_help(self):
        help_message = """
        Доступні команди:
        - add: Додати нову нотатку
        - search: Пошук нотаток
        - sort: Сортувати нотатки за тегом
        - remove: Видалити нотатку
        - edit: Редагувати нотатку
        - save: Зберегти нотатки
        - load: Завантажити нотатки
        - display: Відобразити всі нотатки
        """
        print_message(help_message, 'HELP')