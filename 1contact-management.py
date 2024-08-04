import re
contacts = {}


def print_menu():
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")


def user_input(prompt,regex_pattern=None):
    while True:
        user_input = input(prompt).strip()
        if regex_pattern:
            if not re.match(regex_pattern,user_input):
                print("Please enter a valid input")
                continue
        return user_input
def add_contact():
    email = user_input("Enter the contact's email: ", r"^[\w\.-]+@[\w\.-]+$")
    if email in contacts:
        print("Email already exists")
        return
    name = user_input("Enter contact name: ")
    phone = user_input("Enter contact phone number: ", r"^\+?[1-9]\d{1,14}$")
    address = user_input("Enter contact's address: ")
    notes = user_input("Enter any additional notes: ")


    contacts[email] = {
        "Name": name,
        "Phone number": phone,
        "Address": address,
        "Notes": notes
    }
    print("Contact added successfully!")


def edit_contact():
    email = input("Enter the email for the contact you would like to edit: ", r"^[\w\.-]+@[\w\.-]+$")
    if email:
        if email not in contacts:
            print("Contact does not exist")
            return
    
    print("Leave section blank if you would not like to change anything")
    name = user_input(f"Enter the new name for your contact. current: {contacts[email]['Name']}: ")
    phone = user_input(f"Enter the new phone number for your contact. current: {contacts[email]['Phone number']}: ")
    address = user_input(f"Enter the new address for your contact. current: {contacts[email]['Address']}: ")
    notes = user_input(f"Enter new notes for your contact. current: {contacts[email]['Notes']}: ")
   
    if name:
        contacts[email]['Name'] = name
    if phone:
        contacts[email]['Phone number'] = phone
    if address:
        contacts[email]['Address'] = address
    if notes:
        contacts[email]['Notes'] = notes

    contacts[email] = {
        "Name": name,
        "Phone number": phone,
        "Address": address,
        "Notes": notes
    }
    print("contact updated successfully")


def delete_contact():
    delete = user_input("Enter the email of the contact you would you like to delete: ", r"^[\w\.-]+@[\w\.-]+$")
    if delete not in contacts:
        print("Contact does not exist")
    elif delete in contacts:
        choice = input("Is this the contact you would like to delete?(y/n): ").lower()
        if choice == "y":
            del contacts[delete]
            print("Contact deleted successful")
   
def search_contact():
    search = user_input("Enter the email of the contact you would like to display: " ,  r"^[\w\.-]+@[\w\.-]+$")
    if search not in contacts:
        print("This contact does not exist")
        return
    contact = contacts[search]
    print(f"Email: {search}")
    print(f"Name: {contact['Name']}")
    print(f"Phone Number: {contact['Phone number']}")
    print(f"Address: {contact['Address']}")
    print(f"Notes: {contact['Notes']}")


def display_all_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for email, details in contacts.items():
        print(f"\nEmail: {email}")
        print(f"Name: {details['Name']}")
        print(f"Phone number: {details['Phone number']}")
        print(f"Address: {details['Address']}")
        print(f"Notes: {details['Notes']}")


def export_file():
    filename = user_input("Enter a file name to export the files to") +".txt"
    with open(filename, "w") as file:
        for email, details, in contacts.items():
            file.write(f"Email: {email}\n")
            file.write(f"Name: {details['Name']}\n")
            file.write(f"Phone number: {details['Phone number']}\n")
            file.write(f"Address: {details['Address']}\n")
            file.write(f"Notes: {details['Notes']}\n\n")
    print(f"Contacts exported to {filename}")


def import_file():
    filename = user_input("Enter the file name you would like to import contacts from: ") + ".txt"
    try:
        with open(filename, 'r') as file:
            content = file.read()
            contact = content.strip().split("\n\n")
            for entry in contact:
                lines = entry.split("\n")
                email = lines[0].split(": ")[1]
                if email in contacts:
                    print(f"Contact with email {email} already exists. Skipping.")
                    continue
                contacts[email] = {
                    'Name': lines[1].split(": ")[1],
                    'Phone number': lines[2].split(": ")[1],
                    'Address': lines[3].split(": ")[1],
                    'Notes': lines[4].split(": ")[1]
                }
        print(f"Contacts imported from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

while True:
    print_menu()
   
    choice = user_input("What would you like to do: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        edit_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        export_file()
    elif choice == "7":
        import_file()
    elif choice == "8":
        break
    else:
        print("Please enter a valid input")

