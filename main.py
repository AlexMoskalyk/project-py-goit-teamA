import sys
from prompt_toolkit import prompt
from src.prompt_toolkit_helpers import completer
from src.contacts_book import ContactsBook
from src.notifications import print_message
from src.notes import  NoteBook
from src.contact_note_functions import ( 
    check_cancel,
    add_contact_interactive,
    edit_contact_phone,
    delete_contact_phone,
    edit_contact_email, 
    edit_contact_birthday, 
    edit_contact_address, 
    helper, 
    add_note_interactive, 
    edit_note_interactive
)

def main():
    """Головна функція для запуску термінального помічника."""

    book = ContactsBook()
    notebook = NoteBook()

    print("Welcome to the Contact Book Assistant!")
    notebook.load_notes(show_message = False)
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
                notebook.save_notes(show_message = False)
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
