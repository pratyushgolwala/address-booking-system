"""UC4: Delete Contact Feature - Utility functions for deleting contacts."""

from contacts import Contact


def delete_contact_from_book(address_book_system, book_name, contact):
    """
    Delete a contact from a specific address book.
    
    Args:
        address_book_system: The AddressBookSystem instance
        book_name: Name of the address book
        contact: Contact object to delete
        
    Returns:
        bool: True if deleted, False otherwise
    """
    address_book = address_book_system.get_address_book(book_name)
    if address_book:
        return address_book.remove_contact(contact)
    print(f"Address book '{book_name}' not found.")
    return False


def delete_contact_by_name(address_book_system, book_name, first_name, last_name):
    """
    Delete a contact by first and last name from a specific address book.
    
    Args:
        address_book_system: The AddressBookSystem instance
        book_name: Name of the address book
        first_name: Contact's first name
        last_name: Contact's last name
        
    Returns:
        bool: True if deleted, False otherwise
    """
    address_book = address_book_system.get_address_book(book_name)
    if not address_book:
        print(f"Address book '{book_name}' not found.")
        return False
    
    # Create a dummy contact for comparison (uses __eq__ which compares names)
    dummy_contact = Contact(first_name, last_name, "", "", "", "", "", "")
    return address_book.remove_contact(dummy_contact)


def delete_all_contacts(address_book_system, book_name):
    """
    Delete all contacts from a specific address book.
    
    Args:
        address_book_system: The AddressBookSystem instance
        book_name: Name of the address book
        
    Returns:
        int: Number of contacts deleted
    """
    address_book = address_book_system.get_address_book(book_name)
    if not address_book:
        print(f"Address book '{book_name}' not found.")
        return 0
    
    count = len(address_book.contacts)
    address_book.contacts.clear()
    print(f"Deleted {count} contacts from '{book_name}'.")
    return count
