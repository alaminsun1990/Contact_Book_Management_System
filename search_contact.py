import csv
def search_contact(phone_number):
    with open("all_contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        contact_books = [row for row in reader]
    contact_found = False
    for contact in contact_books:
        if int(contact['phone_number']) == phone_number:
            contact_found = True
            break
    
    if contact_found:
        print(f"{contact['name']}, {contact['email']}, {contact['phone_number']}, {contact['address']}")
    else:
        print(f"No contact found with Phone Number {phone_number}.")