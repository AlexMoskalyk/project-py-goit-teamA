
import sys
import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
# Додаємо поточний шлях до sys.path 
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.contacts_book import ContactsBook, input_error, add_contact, Phone, Email, Birthday, Name,Address
from src.notifications import print_message
from src.notes import Note, NoteBook, Title

# Список ключових слів для автозаповнення
keywords = [
    'add contact', 'show contacts', 'find contact', 'delete contact',
    'edit contact email', 'edit contact phone', 'delete contact phone',
    'contacts birthdays', 'add note', 'show notes', 'find note',
    'edit note', 'delete note', 'sort notes', 'cancel','help', 'exit' 
]
completer = WordCompleter(keywords, ignore_case=True)

def helper():
    """Виводить список доступних команд."""
    commands = {
        "add contact": "Додати новий контакт.",
        "show contacts": "Показати всі контакти.",
        "find contact": "Знайти контакт за іменем.",
        "delete contact": "Видалити контакт за іменем.",
        "edit contact email": "Змінити email контакту",
        "edit contact phone": "Змінити номер телефону контакту.",
        "delete contact phone": "Видалити номер телефону контакту.",
        "contacts birthdays": "Показати контакти з майбутніми днями народження.",
        "edit contact birthday": "Edit a birthday day in contact",
        "edit contact address": "Edit a address in contact",
        "add note": "Додати нову нотатку",
        "show notes": "Показати всі нотатки.",
        "find note": "Пошук нотатки",
        "edit note": "Редагування нотатки",
        "delete note": "Видалення нотатки",
        "sort notes": "Сортування нотаток за тегом",
        "cancel": "Скасування операцій.",
        "help": "Показати список доступних команд.",
        "exit": "Вийти з програми.",
    }
    print("\nAvailable commands:")
    for command, description in commands.items():
        print(f"  {command:15} - {description}")

def check_cancel(input_text: str):
    """Перевіряє, чи ввів користувач команду скасування."""
    if input_text.strip().lower() == "cancel":
        raise KeyboardInterrupt("Операція була скасована.")

@input_error
def add_contact_interactive(book):
    """Додавання контакта."""
  
    while True:
        try:
            name_input = input("Enter name (or type 'cancel' to stop): ").strip()
            check_cancel(name_input)
            name = Name(name_input)
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    while True:
        try:
            phone_input = input("Enter phone (or type 'cancel' to stop): ").strip()
            check_cancel(phone_input)
            phone = Phone(phone_input)
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    while True:
        try:
            email_input = input("Enter email (optional, or type 'cancel' to stop): ").strip()
            check_cancel(email_input)
            email = Email(email_input) if email_input else None
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    while True:
        try:
            address_input = input("Enter address (or type 'cancel' to stop): ").strip()
            check_cancel(address_input)
            address = Address(address_input)
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    while True:
        try:
            birthday_input = input("Enter birthday (DD.MM.YYYY, optional, or type 'cancel' to stop): ").strip()
            check_cancel(birthday_input)
            birthday = Birthday(birthday_input) if birthday_input else None
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    args = [
        name.value,
        phone.value,
        email.value if email else None,
        address.value,
        birthday.value.strftime("%d.%m.%Y") if birthday else None
    ]

    add_contact(args, book)

@input_error
def edit_contact_phone(book):
    name = input("Enter the contact's name to edit the phone number (or type 'cancel' to stop): ").strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}." , 'ERROR')

    new_phone = input("Enter the new phone number (or type 'cancel' to stop): ").strip()
    check_cancel(new_phone)
    record.edit_phone(new_phone)
    return print_message(f"Phone number for {name} updated successfully." , 'SUCCESS')

@input_error
def edit_contact_email(book):
    name = input("Enter the contact's name to edit the email (or type 'cancel' to stop): ").strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}.)", 'ERROR')
    
    new_email = input("Enter the new email (or type 'cancel' to stop): ").strip()
    check_cancel(new_email)
    record.edit_email(new_email)
    return print_message(f"Email for {name} updated successfully.", 'SUCCESS')

@input_error
def edit_contact_birthday(book):
    name = input("Enter the contact's name to edit the birthday date (or type 'cancel' to stop): ").strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}.)", 'ERROR')
    
    new_birthday = input("Enter the new birthday date (or type 'cancel' to stop): ").strip()
    check_cancel(new_birthday)
    record.edit_birthday(new_birthday)
    return print_message(f"Birthday date for {name} have been successfully updated.", 'SUCCESS')

@input_error
def edit_contact_address(book):
    name = input("Enter the contact's name to edit the address (or type 'cancel' to stop): ").strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}.)", 'ERROR')
    
    new_address = input("Enter the new address (or type 'cancel' to stop): ").strip()
    check_cancel(new_address)
    record.edit_address(new_address)
    return print_message(f"A new address for {name} have been successfully updated.", 'SUCCESS')

@input_error
def delete_contact_phone(book):
    name = input("Enter the contact's name to delete a phone number (or type 'cancel' to stop): ").strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}." , 'ERROR')

    phone_to_remove = input("Enter the phone number to remove (or type 'cancel' to stop): ").strip()
    check_cancel(phone_to_remove)
    record.remove_phone(phone_to_remove)
    return print_message(f"Phone number {phone_to_remove} removed for {name}."  , 'SUCCESS')

@input_error
def add_note_interactive(notebook):
    """Додавання нотатки."""
    while True:
        try:
            print_message("Title (or type 'cancel' to stop): ", 'INPUT','') 
            title = input().strip()
            check_cancel(title)
            title = Title(title)    
            break
        except ValueError as e:
            print_message(e, 'ERROR')

    print_message("Note text (or type 'cancel' to stop): ", 'INPUT','') 
    text = input().strip()
    check_cancel(text)

    print_message("Tags (comma separated, or type 'cancel' to stop): ", 'INPUT','')
    tags = [tag.strip() for tag in input().split(',')]
    check_cancel("")
       
    note = Note(title, text, tags)
    notebook.add_note(note)

@input_error
def edit_note_interactive(notebook):
    while True:
        print_message("Old note title (or type 'cancel' to stop): ", 'INPUT','') 
        old_title = input().strip()
        check_cancel(old_title)
        if notebook.note_exists(old_title):
            break
        print_message("Note not found.", 'ERROR')

    while True:
        try:
            print_message("New note title (or type 'cancel' to stop): ", 'INPUT','') 
            new_title = input().strip()
            check_cancel(new_title)
            new_title = Title(new_title)    
            break
        except ValueError as e:
            print_message(e, 'ERROR')

    print_message("New note text (or type 'cancel' to stop): ", 'INPUT','') 
    new_text = input().strip()
    check_cancel(new_text)

    print_message("New tags (comma separated, or type 'cancel' to stop): ", 'INPUT','')
    new_tags = [tag.strip() for tag in input().split(',')]
    check_cancel("")
    
    notebook.edit_note(old_title, new_title, new_text, new_tags)

def main():
    """Головна функція для запуску термінального помічника."""

    book = ContactsBook()
    notebook = NoteBook()

    print("Welcome to the Contact Book Assistant!")
    notebook.load_notes(show_error = False)
    book.load_contacts_book()
    print("Type 'help' to see the list of available commands.")

    while True:
        try:
            command = prompt("Enter command: ", completer=completer).strip().lower()
            check_cancel(command)

            if command == "add contact":
                add_contact_interactive(book)

            elif command == "edit contact phone":
                edit_contact_phone(book)

            elif command == "delete contact phone":
               delete_contact_phone(book)

            elif command == "edit contact email":
                edit_contact_email(book)

            elif command == "show contacts":
                book.display_contacts()

            elif command == "find contact":
                name = input("Enter name to find (or type 'cancel' to stop): ").strip()
                check_cancel(name)
                record = book.find(name)


            elif command == "delete contact":
                name = input("Enter name to delete (or type 'cancel' to stop): ").strip()
                check_cancel(name)
                book.delete(name)


            elif command == "contacts birthdays":
                upcoming = book.get_upcoming_birthdays()
                if not upcoming:
                    print("No upcoming birthdays.")
                else:
                    for record in upcoming:
                        print(record)

            elif command == "edit contact birthday":
                edit_contact_birthday(book)

            elif command == "edit contact address":
                edit_contact_address(book)

            elif command == "help":
                helper()

            elif command == "exit":
                book.save_contacts_book()
                notebook.save_notes(show_error = False)
                print("Goodbye!")
                sys.exit()

            elif command == 'add note':
                add_note_interactive(notebook)

            elif command == 'find note':
                print_message("Enter query (or type 'cancel' to stop): ", 'INPUT','')
                query = input()
                check_cancel(query)
                results = notebook.search_notes(query)
                for note in results:
                    print(note)

            elif command == 'delete note':
                print_message("Note text (or type 'cancel' to stop): ", 'INPUT','')
                text = input()
                check_cancel(text)
                notebook.remove_note(text)

            elif command == 'edit note':
                edit_note_interactive(notebook)

            elif command == 'sort notes':
                print_message("Tag to sort by (or type 'cancel' to stop): ", 'INPUT', '')
                tag = input() 
                check_cancel(tag)
                sorted_notes = notebook.sort_notes_by_tag(tag)
                for note in sorted_notes:
                    print_message(str(note), 'SUCCESS')         

            elif command == 'show notes':
                notebook.display_notes()

            else:
                print_message("Unknown command. Type 'help' to see available commands.",'ERROR')

        except KeyboardInterrupt:
            print_message("\nOperation cancelled. Returning to main menu.", 'WARNING')
        except Exception as e:
            print_message(f"Error: {e}", 'ERROR')

if __name__ == "__main__":
    main()
