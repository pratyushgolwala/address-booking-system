"""UC6: Main Console - Interactive Address Book System."""

from contacts import Contact
from address_book import AddressBook
from address_book_system import AddressBookSystem
from delete_contact import delete_contact_by_name, delete_all_contacts
from search_by_name import search_by_name_all_books, display_search_results


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("       ADDRESS BOOK SYSTEM")
    print("=" * 50)
    print("1.  Create Address Book")
    print("2.  Delete Address Book")
    print("3.  List All Address Books")
    print("4.  Add Contact")
    print("5.  Delete Contact")
    print("6.  Delete All Contacts from Address Book")
    print("7.  Edit Contact")
    print("8.  Display All Contacts")
    print("9.  Display Contacts in Address Book")
    print("10. Search Contact by Name")
    print("0.  Exit")
    print("=" * 50)


def get_contact_input():
    """Get contact details from user."""
    print("\nEnter contact details:")
    first_name = input("  First Name: ").strip()
    last_name = input("  Last Name: ").strip()
    address = input("  Address: ").strip()
    city = input("  City: ").strip()
    state = input("  State: ").strip()
    zip_code = input("  ZIP Code: ").strip()
    phone_number = input("  Phone Number: ").strip()
    email = input("  Email: ").strip()
    
    return Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)


def select_address_book(system):
    """Let user select an address book."""
    books = system.list_address_books()
    if not books:
        print("No address books available. Create one first.")
        return None
    
    print("\nAvailable Address Books:")
    for i, name in enumerate(books, 1):
        print(f"  {i}. {name}")
    
    try:
        choice = int(input("Select address book (number): "))
        if 1 <= choice <= len(books):
            return books[choice - 1]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input.")
        return None


def create_address_book(system):
    """Create a new address book."""
    name = input("\nEnter address book name: ").strip()
    if name:
        system.create_address_book(name)
    else:
        print("Name cannot be empty.")


def delete_address_book(system):
    """Delete an address book."""
    book_name = select_address_book(system)
    if book_name:
        confirm = input(f"Are you sure you want to delete '{book_name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            system.delete_address_book(book_name)


def add_contact(system):
    """Add a contact to an address book."""
    book_name = select_address_book(system)
    if book_name:
        contact = get_contact_input()
        address_book = system.get_address_book(book_name)
        address_book.add_contact(contact)


def delete_contact(system):
    """Delete a contact from an address book."""
    book_name = select_address_book(system)
    if book_name:
        first_name = input("  Enter contact's First Name: ").strip()
        last_name = input("  Enter contact's Last Name: ").strip()
        delete_contact_by_name(system, book_name, first_name, last_name)


def delete_all(system):
    """Delete all contacts from an address book."""
    book_name = select_address_book(system)
    if book_name:
        confirm = input(f"Delete ALL contacts from '{book_name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            delete_all_contacts(system, book_name)


def edit_contact(system):
    """Edit a contact in an address book."""
    book_name = select_address_book(system)
    if book_name:
        print("\nEnter current contact name to edit:")
        old_first = input("  First Name: ").strip()
        old_last = input("  Last Name: ").strip()
        
        address_book = system.get_address_book(book_name)
        old_contact = Contact(old_first, old_last, "", "", "", "", "", "")
        
        if old_contact in address_book.contacts:
            print("\nEnter new contact details:")
            new_contact = get_contact_input()
            address_book.edit_contact(old_contact, new_contact)
        else:
            print(f"Contact {old_first} {old_last} not found.")


def display_book_contacts(system):
    """Display contacts in a specific address book."""
    book_name = select_address_book(system)
    if book_name:
        address_book = system.get_address_book(book_name)
        address_book.display_contacts()


def search_contact(system):
    """Search for contacts by name."""
    name = input("\nEnter name to search: ").strip()
    if name:
        results = search_by_name_all_books(system, name)
        display_search_results(results)


def main():
    """Main function - runs the interactive console."""
    system = AddressBookSystem()
    
    while True:
        print_menu()
        try:
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                create_address_book(system)
            elif choice == '2':
                delete_address_book(system)
            elif choice == '3':
                books = system.list_address_books()
                if books:
                    print("\nAddress Books:", ", ".join(books))
                else:
                    print("\nNo address books created yet.")
            elif choice == '4':
                add_contact(system)
            elif choice == '5':
                delete_contact(system)
            elif choice == '6':
                delete_all(system)
            elif choice == '7':
                edit_contact(system)
            elif choice == '8':
                system.display_all_address_books()
            elif choice == '9':
                display_book_contacts(system)
            elif choice == '10':
                search_contact(system)
            elif choice == '0':
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()

