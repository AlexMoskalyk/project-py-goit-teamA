# Contacts and Notes Management System

This project is a Python-based system for managing contacts and notes.

## Features

1. **Contact Management**

   - Add new contacts
   - Edit existing contacts
   - Delete contacts
   - Search for contacts

2. **Notes Management**

   - Create new notes with text content
   - Add tags to notes
   - Edit existing notes
   - Delete notes
   - Search for notes by title

3. **Data Persistence**

   - Contacts and notes are saved to disk (using pickle)
   - Data is automatically loaded when the program starts

4. **User Interface**
   - Command-line interface for interacting with the system

## Usage

To use the Contacts and Notes Management System, follow these steps:

1. **Starting the Program**
   Run the main script from your command line: `python main.py`

2. **Using Commands**
   Once the program is running, you can enter commands to manage contacts and notes. Here are some examples:

- To add a new contact:

`add contact`

Follow the prompts to enter the contact's details.

- To view all contacts:

  `show contacts`

- To find a specific contact:

  `find contact`

  Enter the name when prompted.

- To add a new note:

  `add note`

  Enter the note text and tags as prompted.

- To view all notes:

  `show notes`

- To sort notes by tag:

  `sort notes`

  Enter the tag when prompted.

3. **Editing and Deleting**

- To edit a contact's email:

  `edit contact email`

  Follow the prompts to select the contact and enter the new email.

- To delete a contact:

  `delete contact`

  Enter the name of the contact to delete when prompted.

- To edit a note:

  `edit note`

  Follow the prompts to select and edit the note.

4. **Getting Help**
   If you need to see the list of available commands at any time, enter: `help`

5. **Exiting the Program**
   To save your changes and exit the program, enter: `exit`

Remember, you can always use the `cancel` command to abort an operation in progress.

Note: All changes are automatically saved when you exit the program or after each operation.
