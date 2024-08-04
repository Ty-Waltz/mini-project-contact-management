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

def sorted_contacts():
    return dict(sorted(contacts.items(), key=lambda item: item[0].lower()))
    

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
    category = user_input("Enter the category for your contact: ")

    contacts[email] = {
        "Name": name,
        "Phone number": phone,
        "Address": address,
        "Notes": notes,
        "Category": category
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
    category = user_input(f"Enter new category for your contact. current: {contacts[email]['Category']}: ")
    if name:
        contacts[email]['Name'] = name
    if phone:
        contacts[email]['Phone number'] = phone
    if address:
        contacts[email]['Address'] = address
    if notes:
        contacts[email]['Notes'] = notes
    if category:
        contacts[email]['Category'] = category

    print("contact updated successfully")


def delete_contact():
    delete = user_input("Enter the email of the contact you would you like to delete: ", r"^[\w\.-]+@[\w\.-]+$")
    if delete not in contacts:
        print("Contact does not exist")
    del contacts[delete]
    print("Contact deleted successfully")
   
def search_contact():
    search = user_input("Enter any details of the contact you would like to display: ").strip().lower()
    results = False
    
    for email, details in contacts.items(): 
        if (search in email or
            search in details['name'].lower() or
            search in details['Phone number'].lower() or
            search in details['Address'].lower() or
            search in details['Notes'].lower() or
            search in details['Category'].lower()):
            print(f"Email: {email}")
            print(f"Name: {details['Name']}")
            print(f"Phone: {details['Phone number']}")
            print(f"Address: {details['Address']}")
            print(f"Notes: {details['Notes']}")
            print(f"Category: {details['Category']}")
            results = True
    if not results:
        print("Results not found")

def display_all_contacts():
    sorted_list = sorted_contacts()
    if not sorted_list:
        print("No contacts available.")
        return
    for email, details in sorted_list.items():
        print(f"\nEmail: {email}")
        print(f"Name: {details['Name']}")
        print(f"Phone number: {details['Phone number']}")
        print(f"Address: {details['Address']}")
        print(f"Notes: {details['Notes']}")
        print(f"Category: {details['Category']}")


def export_file():
    filename = user_input("Enter a file name to export the files to: ") +".txt"
    with open(filename, "w") as file:
        for email, details in contacts.items():
            file.write(f"Email: {email}\n")
            file.write(f"Name: {details['Name']}\n")
            file.write(f"Phone number: {details['Phone number']}\n")
            file.write(f"Address: {details['Address']}\n")
            file.write(f"Notes: {details['Notes']}\n\n")
            file.write(f"Category: {details['Category']}\n\n")
    print(f"Contacts exported to {filename}")


def import_file():
    filename = user_input("Enter the file name you would like to import contacts from: ") + ".txt"
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            contact = content.split("\n\n")
            for entry in contact:
                lines = entry.split("\n")
                if len(lines) < 6: 
                    print(f"Skipping malformed entry: {entry}")
                    continue
                
                email = lines[0].split(": ")[1].strip()
                if email in contacts:
                    print(f"Contact with email {email} already exists. Skipping.")
                    continue
                
                
                contacts[email] = {
                    'Name': lines[1].split(": ")[1].strip() if len(lines) > 1 else 'N/A',
                    'Phone number': lines[2].split(": ")[1].strip() if len(lines) > 2 else 'N/A',
                    'Address': lines[3].split(": ")[1].strip() if len(lines) > 3 else 'N/A',
                    'Notes': lines[4].split(": ")[1].strip() if len(lines) > 4 else 'N/A',
                    'Category': lines[5].split(": ")[1].strip() if len(lines) > 5 else 'N/A'
                }
        print(f"Contacts imported from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

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
