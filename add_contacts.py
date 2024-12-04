
from save_all_contacts import save_all_contacts

def save_contacts(contact_books):
    name= input("Enter Contact Name: ")
    email= input("Enter Contact Email: ")
    phone_number= int(input("Enter Contact Number: "))
    address= input("Enter Address: ")

    for contact in contact_books:
        if contact["phone_number"] == phone_number:
            print("Error: Phone number already exists. Please try again with a unique number.")
            return

    contact_book = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "address": address
    }

    contact_books.append(contact_book)
    save_all_contacts(contact_books)

    print("Contact Added Successfully")

    return contact_books