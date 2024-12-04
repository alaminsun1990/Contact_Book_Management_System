import csv
def save_all_contacts(contact_books):
    with open("all_contacts.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone_number", "address"])
        writer.writeheader()
        writer.writerows(contact_books)
