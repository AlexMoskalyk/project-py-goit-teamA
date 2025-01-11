from src.contacts_book import input_error, add_contact, Phone, Email, Birthday, Name,Address
from src.notifications import print_message
from src.notes import Note, Title
from src.helpers import input_error, check_cancel

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
    print_message("\nAvailable commands:", "HELP")
    for command, description in commands.items():
        print_message(f"  {command:15} - {description}","HELP")

@input_error
def add_contact_interactive(book):
    """Додавання контакта."""
  
    while True:
        try:
            print_message("Enter name (or type 'cancel' to stop): ", 'INPUT', end='')
            name_input = input().strip()
            check_cancel(name_input)
            name = Name(name_input)
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    while True:
        try:
            print_message("Enter phone (or type 'cancel' to stop): ", 'INPUT', end='')
            phone_input = input().strip()
            check_cancel(phone_input)
            phone = Phone(phone_input)
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    while True:
        try:
            print_message("Enter email (optional, or type 'cancel' to stop): ", 'INPUT', end='')
            email_input = input().strip()
            check_cancel(email_input)
            email = Email(email_input) if email_input else None
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    while True:
        try:
            print_message("Enter address (or type 'cancel' to stop): ", 'INPUT', end='')
            address_input = input().strip()
            check_cancel(address_input)
            address = Address(address_input)
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

    while True:
        try:
            print_message("Enter birthday (DD.MM.YYYY, optional, or type 'cancel' to stop): ", 'INPUT', end='')
            birthday_input = input().strip()
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
    print_message("Enter the contact's name to edit the phone number (or type 'cancel' to stop): ", 'INPUT', end='')
    name = input().strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}." , 'ERROR')
    

    print_message("Enter the new phone number (or type 'cancel' to stop): ", 'INPUT', end='')
    new_phone = input().strip()
    check_cancel(new_phone)
    record.edit_phone(new_phone)
    return print_message(f"Phone number for {name} updated successfully." , 'SUCCESS')

@input_error
def edit_contact_email(book):

    print_message("Enter the contact's name to edit the email (or type 'cancel' to stop): ", 'INPUT', end='')
    name = input().strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}.)", 'ERROR')
    
    print_message("Enter the new email (or type 'cancel' to stop): ", 'INPUT', end='')
    new_email = input().strip()
    check_cancel(new_email)
    record.edit_email(new_email)
    return print_message(f"Email for {name} updated successfully.", 'SUCCESS')

@input_error
def edit_contact_birthday(book):
    print_message("Enter the contact's name to edit the birthday date (or type 'cancel' to stop): ", 'INPUT', end='')
    name = input().strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}.)", 'ERROR')
    
    print_message("Enter the new birthday date (or type 'cancel' to stop): ", 'INPUT', end='')
    new_birthday = input().strip()
    check_cancel(new_birthday)
    record.edit_birthday(new_birthday)
    return print_message(f"Birthday date for {name} have been successfully updated.", 'SUCCESS')

@input_error
def edit_contact_address(book):
    print_message("Enter the contact's name to edit the address (or type 'cancel' to stop): ", 'INPUT', end='')
    name = input().strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}.)", 'ERROR')
    
    print_message("Enter the new address (or type 'cancel' to stop): ", 'INPUT', end='')
    new_address = input().strip()
    check_cancel(new_address)
    record.edit_address(new_address)
    return print_message(f"A new address for {name} have been successfully updated.", 'SUCCESS')

@input_error
def delete_contact_phone(book):
    print_message("Enter the contact's name to delete a phone number (or type 'cancel' to stop): ", 'INPUT', end='')
    name = input().strip()
    check_cancel(name)
    record = book.find(name)
    if not record:
        return print_message(f"No contact found with the name {name}." , 'ERROR')

    print_message("Enter the phone number to remove (or type 'cancel' to stop): ", 'INPUT', end='')
    phone_to_remove = input().strip()
    check_cancel(phone_to_remove)
    record.remove_phone(phone_to_remove)
    return print_message(f"Phone number {phone_to_remove} removed for {name}."  , 'SUCCESS')

@input_error
def add_note_interactive(notebook):
    """Додавання нотатки."""
    while True:
        try:
            print_message("Title (or type 'cancel' to stop): ", 'INPUT','')
            title = input()
            check_cancel(title)
            title = Title(title.strip())    
            break
        except ValueError as e:
            print_message(str(e), 'ERROR')

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
            print_message(str(e), 'ERROR')

    print_message("New note text (or type 'cancel' to stop): ", 'INPUT','')
    new_text = input().strip()
    check_cancel(new_text)

    print_message("New tags (comma separated, or type 'cancel' to stop): ", 'INPUT','')
    new_tags = [tag.strip() for tag in input().split(',')]
    check_cancel("")
    
    notebook.edit_note(old_title, new_title, new_text, new_tags)