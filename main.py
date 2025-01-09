
import sys
import os
# Додаємо поточний шлях до sys.path 
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.contacts_book import ContactsBook, input_error, add_contact, Phone, Email, Birthday, Name,Address
from src.notifications import print_message
from src.notes import Note, NoteBook, TextNote

def helper():
    """Виводить список доступних команд."""
    commands = {
        "add": "Додати новий контакт.",
        "show": "Показати всі контакти.",
        "find": "Знайти контакт за іменем.",
        "delete": "Видалити контакт за іменем.",
        "edit email": "Змінити email контакту",
        "edit phone": "Змінити номер телефону контакту.",
        "delete phone": "Видалити номер телефону контакту.",
        "birthdays": "Показати контакти з майбутніми днями народження.",
        "add note": "Додати нову нотатку",
        "show notes": "Показати всі нотатки.",
        "find note": "Пошук нотатки",
        "edit note": "Редагування нотатки",
        "del note": "Видалення нотатки",
        "sort notes": "Сортування нотаток за тегом",
        "help": "Показати список доступних команд.",
        "exit": "Вийти з програми.",
    }
    print("\nAvailable commands:")
    for command, description in commands.items():
        print(f"  {command:15} - {description}")


@input_error
def add_contact_interactive(book):
    """Додавання контакта."""
  
    while True:
        try:
            name = Name(input("Enter name: ").strip())
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            phone = Phone(input("Enter phone: ").strip())
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            email_input = input("Enter email (optional): ").strip()
            email = Email(email_input) if email_input else None
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            address = Address(input("Enter address: ").strip())
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            birthday_input = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
            birthday = Birthday(birthday_input) if birthday_input else None
            break
        except ValueError as e:
            print(e)

    args = [
        name.value,
        phone.value,
        email.value if email else None,
        address.value,
        birthday.value.strftime("%d.%m.%Y") if birthday else None
    ]

    print(add_contact(args, book))



@input_error
def edit_contact_phone(book):
    name = input("Enter the contact's name to edit the phone number: ").strip()
    record = book.find(name)
    if not record:
        return f"No contact found with the name {name}."

    new_phone = input("Enter the new phone number: ").strip()
    record.edit_phone(new_phone)
    return f"Phone number for {name} updated successfully."

@input_error
def edit_contact_email(book):
    name = input("Enter the contact's name to edit the email: ").strip()
    record = book.find(name)
    if not record:
        return f"No contact found with the name {name}."
    
    new_email = input("Enter the new email: ").strip()
    record.edit_email(new_email)
    return f"Email for {name} updated successfully."

@input_error
def delete_contact_phone(book):
    name = input("Enter the contact's name to delete a phone number: ").strip()
    record = book.find(name)
    if not record:
        return f"No contact found with the name {name}."

    phone_to_remove = input("Enter the phone number to remove: ").strip()
    record.remove_phone(phone_to_remove)
    return f"Phone number {phone_to_remove} removed for {name}."

@input_error
def add_note_interactive(notebook):
    """Додавання нотатки."""
    while True:
        try:
            print_message("Note text: ", 'INPUT','') 
            text = TextNote(input().strip())    
            break
        except ValueError as e:
            print_message(e, 'ERROR')

    while True:
        try:
            print_message("Tags (comma separated): ", 'INPUT','')
            tags = input().split(',')
            break
        except ValueError as e:
            print(e)

    note = Note(text, tags)
    notebook.add_note(note)

def main():
    """Головна функція для запуску термінального помічника."""

    book = ContactsBook()
    notebook = NoteBook()
    notebook.load_notes()

    print("Welcome to the Contact Book Assistant!")
    print("Type 'help' to see the list of available commands.")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "add":
            add_contact_interactive(book)

        elif command == "edit phone":
            print(edit_contact_phone(book))

        elif command == "delete phone":
            print(delete_contact_phone(book))

        elif command == "edit email":
            print(edit_contact_email(book))

        elif command == "show":
            if not book.data:
                print("Contact book is empty.")
            else:
                for record in book.values():
                    print(record)

        elif command == "find":
            name = input("Enter name to find: ").strip()
            record = book.find(name)
            if record:
                print(record)
            else:
                print(f"No contact found with the name {name}.")

        elif command == "delete":
            name = input("Enter name to delete: ").strip()
            if name in book.data:
                book.delete(name)
                print(f"Contact {name} deleted.")
            else:
                print(f"No contact found with the name {name}.")

        elif command == "birthdays":
            upcoming = book.get_upcoming_birthdays()
            if not upcoming:
                print("No upcoming birthdays.")
            else:
                for record in upcoming:
                    print(record)

        elif command == "help":
            helper()

        elif command == "exit":
            notebook.save_notes()
            print("Goodbye!")
            sys.exit()
        elif command == 'add note':
            add_note_interactive(notebook)
        elif command == 'find note':
            print_message("Enter query: ", 'INPUT','')
            query = input()
            results = notebook.search_notes(query)
            for note in results:
                print(note)
        elif command == 'del note':
            print_message("Note text: ", 'INPUT','')
            text = input()
            notebook.remove_note(text)
        elif command == 'edit note':
            print_message("Old note text: ", 'INPUT','')
            old_text = input()
            print_message("New note text: ", 'INPUT', '')
            new_text = input()
            print_message("New tags (comma separated): ", 'INPUT', '')
            new_tags = input().split(',')
            notebook.edit_note(old_text, new_text, new_tags)
        elif command == 'sort notes':
            print_message("Tag to sort by: ", 'INPUT', '')
            tag = input() 
            sorted_notes = notebook.sort_notes_by_tag(tag)
            for note in sorted_notes:
                print_message(str(note), 'SUCCESS')         
        elif command == 'show notes':
            notebook.display_notes()
        else:
            print_message("Unknown command. Type 'help' to see available commands.",'ERROR')


if __name__ == "__main__":
    main()
