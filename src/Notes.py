import pickle
from typing import List
from notifications import print_message

class Note:
    def __init__(self, text: str, tags: List[str] = []):
        self.text = text
        self.tags = tags

    def __str__(self) -> str:
        return f"{self.text} - Теги: {', '.join(self.tags)}"

class NoteBook:
    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self, note: Note):
        self.notes.append(note)
        print_message("Нотатка успішно додана.", 'SUCCESS')

    def search_notes(self, query: str) -> List[Note]:
        return [n for n in self.notes if query.lower() in n.text.lower() or any(query.lower() in tag.lower() for tag in n.tags)]

    def sort_notes_by_tag(self, tag: str) -> List[Note]:
        return sorted([n for n in self.notes if tag.lower() in (t.lower() for t in n.tags)], key=lambda x: x.text)

    def remove_note(self, text: str):
        self.notes = [n for n in self.notes if n.text != text]
        print_message("Нотатка успішно видалена.", 'SUCCESS')

    def edit_note(self, old_text: str, new_text: str, new_tags: List[str]):
        for note in self.notes:
            if note.text == old_text:
                note.text = new_text
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
            print_message("Файл не знайдено, створюємо новий.", 'ERROR')
