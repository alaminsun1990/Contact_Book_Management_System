import csv

def delete_contact(contact_books):
    contact_books = []
    try:
        with open("all_contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            contact_books = [row for row in reader]
    except FileNotFoundError:
        print(f"File not found.")
        return

    print("\nAvailable Contacts:")
    for contact in contact_books:
        print(f"{contact['name']}, {contact['email']}, {contact['phone_number']}, {contact['address']}")
    
    contact_number_to_delete = input("\nEnter the Phone Number of the contact to delete: ")
    

    contact_found = False
    for contact in contact_books:
        if contact['phone_number'] == contact_number_to_delete:
            contact_books.remove(contact)
            contact_found = True
            break
    
    if contact_found:
        # Save the updated contact list back to the CSV file
        with open("all_contacts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email", "phone_number", "address"])
            writer.writeheader()
            writer.writerows(contact_books)
        print(f"Contact with Phone Number {contact_number_to_delete} deleted successfully.")
    else:
        print(f"No contact found with Phone Number {contact_number_to_delete}.")


