import add_contacts
import view_all_contacts
import delete_contact
import search_contact

contact_books= []

while True:
    print("Welcome to Contact Managment System")
    print("0. Exit")
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Delete Contacts")
    print("4. Seach Contacts")

    menu = int(input("Select any number: "))
    if menu == 0:
        print("Thanks for using Library Managment System ")
        break
    elif menu == 1: 
         contact_books = add_contacts.save_contacts(contact_books)
    elif menu == 2:
         view_all_contacts.view_all_contacts(contact_books)
    elif menu == 3:
        contact_books = delete_contact.delete_contact(contact_books)
    elif menu == 4:
        phone_number = int(input("Entry phone number: "))
        search_contact.search_contact(phone_number)
    else:
        print("choose a valid number")


