import pickle
from typing import List
from src.notifications import print_message
from contacts_book import Field

class TextNote(Field):
    """Клас для зберігання тексту нотатки (обов'язкове поле)."""
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Нотатка не може бути порожньою або складатися тільки з пробілів.")
        super().__init__(value.strip())

class Note:
    def __init__(self, text: TextNote, tags: List[str] = []):
        self.text = text
        self.tags = tags

    def __str__(self) -> str:
        return f"{self.text.value} - Теги: {', '.join(self.tags)}"

class NoteBook:
    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self, note: Note):
        self.notes.append(note)
        print_message("Нотатка успішно додана.", 'SUCCESS')

    def search_notes(self, query: str) -> List[Note]:
        results = [n for n in self.notes if query.lower() in n.text.value.lower() or any(query.lower() in tag.lower() for tag in n.tags)] 
        if not results:
             print_message("Нотатки не знайдено.", 'ERROR')
        return results
    
    def sort_notes_by_tag(self, tag: str) -> List[Note]:
        results = sorted([n for n in self.notes if tag.lower() in (t.lower() for t in n.tags)], key=lambda x: x.text.value)
        if not results:
             print_message("Нотатки не знайдено.", 'ERROR')
        return results
    
    def remove_note(self, text: str):
        initial_length = len(self.notes)
        self.notes = [n for n in self.notes if n.text.value != text]
        if len(self.notes) < initial_length:
            print_message("Нотатка успішно видалена.", 'SUCCESS')
        else:
            print_message("Нотатку не знайдено.", 'ERROR')

    def edit_note(self, old_text: str, new_text: str, new_tags: List[str]):
        for note in self.notes:
            if note.text.value == old_text:
                note.text = TextNote(new_text)
                note.tags = new_tags
                print_message("Нотатка успішно відредагована.", 'SUCCESS')
                return
        print_message("Нотатку не знайдено.", 'ERROR')

    def save_notes(self, filename: str = 'notes.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self.notes, file)
        print_message("Нотатки успішно збережені.", 'SUCCESS')

    def load_notes(self, filename: str = 'notes.pkl'):
        try:
            with open(filename, 'rb') as file:
                self.notes = pickle.load(file)
            print_message("Нотатки успішно завантажені.", 'SUCCESS')
        except FileNotFoundError:
            print_message("Немає збережених нотаток.", 'ERROR')

    def display_notes(self):
        if not self.notes:
            print_message("Немає нотаток для відображення.", 'ERROR')
        else:
            for note in self.notes:
                print_message(str(note), 'SUCCESS')
