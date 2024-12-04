import csv
def view_all_contacts(contact_books):
    contact_books = []
    try:
        with open("all_contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            contact_books = [row for row in reader]
            for contact in contact_books:
                print(f"{contact['name']}, {contact['email']}, {contact['phone_number']}, {contact['address']}")
    except FileNotFoundError:
        print(f"File not found. Starting with an empty contact list.")
    return contact_books


    