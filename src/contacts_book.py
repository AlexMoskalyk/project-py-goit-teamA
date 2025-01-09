from collections import UserDict
from datetime import datetime, timedelta
import re
from src.notifications import print_message
import pickle


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Клас для зберігання імені контакту (обов'язкове поле)."""
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Ім'я не може бути порожнім або складатися тільки з пробілів.")
        super().__init__(value.strip())


class Phone(Field):
    """Клас для зберігання номера телефону з валідацією формату (10 цифр)."""
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Номер телефону повинен містити рівно 10 цифр.")
        super().__init__(value)

    @staticmethod
    def validate(value):
        return bool(re.fullmatch(r"\d{10}", value))
    
    def get_value(self):
        """Повертає значення контакту."""
        return self.value


class Email(Field):
    """Клас для зберігання email з валідацією."""
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Невірний формат email.")
        super().__init__(value)

    @staticmethod
    def validate(value):
        return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", value))
    
    def get_value(self):
        """Повертає значення email."""
        return self.value


class Address(Field):
    """Клас для зберігання адреси."""
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Адреса не може бути порожньою.")
        super().__init__(value)


class Birthday(Field):
    """Клас для зберігання дати народження у форматі DD.MM.YYYY."""
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    """Клас для зберігання інформації про контакт."""
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone_number):
        if self.phone:
            raise ValueError(f"Contact {self.name.value} already has a phone number: {self.phone.value}.")
        self.phone = Phone(phone_number)

    def edit_phone(self, new_number):
        if not self.phone:
            raise ValueError(f"Contact {self.name.value} has no phone number to edit.")
        if not Phone.validate(new_number):
            raise ValueError("Новий номер телефону повинен містити рівно 10 цифр.")
        if self.phone.value == new_number:
            raise ValueError("Контакт вже має такий номер телефону")
        self.phone.value = new_number

    def remove_phone(self, phone_number=None):
        
        if not self.phone:
            raise ValueError(f"Contact {self.name.value} has no phone number to remove.")
        if phone_number and self.phone.value != phone_number:
            raise ValueError(f"The phone number {phone_number} does not match the stored phone.")
        self.phone = None

    def add_email(self, email):
        self.email = Email(email)

    def edit_email(self, new_email):
        if not self.email:
            raise ValueError(f"Contact {self.name.value} has no email to edit.")
        if not Email.validate(new_email):
            raise ValueError("Новий email не відповідає формату.")
        if self.email.value == new_email:
            raise ValueError("Контакт вже має такий email")
        self.email.value = new_email

    def add_address(self, address):
        self.address = Address(address)

    def edit_address(self, new_address):
        if not self.address:
            raise ValueError(f"Contact {self.name.value} has no address to edit.")
        if self.address.value == new_address:
            raise ValueError("The same address is already exist")
        self.address.value = new_address

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def edit_birthday(self, new_birthday):
        if not self.birthday:
            raise ValueError(f"Contact {self.name.value} has no birthday to edit.")
        if self.birthday.value == new_birthday:
            raise ValueError(f"Contact {self.name.value} has birthday this birthday already.")
        self.birthday = new_birthday


    def __str__(self):
        phone_str = f", phone: {self.phone}" if self.phone else ""
        birthday_str = f", birthday: {self.birthday}" if self.birthday else ""
        email_str = f", email: {self.email}" if self.email else ""
        address_str = f", address: {self.address}" if self.address else ""
        return f"Contact name: {self.name.value}{phone_str}{birthday_str}{email_str}{address_str}"


class ContactsBook(UserDict):
    """Клас для зберігання та управління записами у книзі контактів."""
    def add_record(self, record):
        self.data[record.name.value] = record
        

    def find(self, name):
        record = self.data.get(name)
        if record:
            print_message(f"Contact found: {record}", 'SUCCESS')
        else:
            print_message(f"No contact found with the name {name}.", 'ERROR')
        return record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print_message(f"Contact {name} deleted successfully.", 'SUCCESS')
        else:
            print_message(f"No contact found with the name {name}.", 'ERROR')

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.today()
        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if today <= birthday_this_year <= today + timedelta(days=7):
                    upcoming_birthdays.append(record)
        if not upcoming_birthdays:
            print_message("No upcoming birthdays found.", 'INFO')
        return upcoming_birthdays
    
    def save_contacts_book(self, filename: str = 'contact_book.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)
        print_message("Contacts successfully saved", 'SUCCESS')

    def load_contacts_book(self, filename: str = 'contact_book.pkl'):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
            print_message("Contacts successfully loaded", 'SUCCESS')
        except FileNotFoundError:
            print_message("No saved contacts found.", 'WARNING')

    def display_contacts(self):
        if not self.data:
            print_message("Contacts is empty", 'ERROR')
        else:
            for contact in self.data.values():
                print_message(str(contact), 'SUCCESS')


def input_error(func):
    """Декоратор для обробки помилок вводу."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError) as e:
            print_message(str(e), 'ERROR')
    return wrapper


@input_error
def add_contact(args, book):
    """Додавання контакту до книги."""

    name, phone, email, address, birthday = args

    record = Record(name)   
    if phone:
        record.add_phone(phone)

    if email:
        record.add_email(email)
    if address:
        record.add_address(address)
    if birthday:
        record.add_birthday(birthday) 
    book.add_record(record)
    print_message(f"Contact {name} added successfully.", 'SUCCESS')