"""UC5: Search by Name Feature - Utility functions for searching contacts by name."""


def search_by_name_in_book(address_book, name):
    """
    Search for contacts by first or last name in a single address book.
    
    Args:
        address_book: The AddressBook instance to search in
        name: Name string to search for (partial match supported)
        
    Returns:
        list: List of matching Contact objects
    """
    results = []
    name_lower = name.lower()
    for contact in address_book.contacts:
        if (name_lower in contact.first_name.lower() or 
            name_lower in contact.last_name.lower()):
            results.append(contact)
    return results


def search_by_name_all_books(address_book_system, name):
    """
    Search for contacts by name across all address books.
    
    Args:
        address_book_system: The AddressBookSystem instance
        name: Name string to search for (partial match supported)
        
    Returns:
        dict: Dictionary with book names as keys and list of matching contacts as values
    """
    results = {}
    for book_name, address_book in address_book_system.address_books.items():
        matches = search_by_name_in_book(address_book, name)
        if matches:
            results[book_name] = matches
    return results


def search_by_full_name(address_book_system, first_name, last_name):
    """
    Search for contacts by exact first and last name across all address books.
    
    Args:
        address_book_system: The AddressBookSystem instance
        first_name: First name to search for
        last_name: Last name to search for
        
    Returns:
        dict: Dictionary with book names as keys and list of matching contacts as values
    """
    results = {}
    for book_name, address_book in address_book_system.address_books.items():
        matches = []
        for contact in address_book.contacts:
            if (contact.first_name.lower() == first_name.lower() and 
                contact.last_name.lower() == last_name.lower()):
                matches.append(contact)
        if matches:
            results[book_name] = matches
    return results


def display_search_results(results):
    """
    Display search results in a formatted way.
    
    Args:
        results: Dictionary with book names as keys and list of contacts as values
    """
    if not results:
        print("No contacts found.")
        return
    
    total = sum(len(contacts) for contacts in results.values())
    print(f"\nFound {total} contact(s):")
    
    for book_name, contacts in results.items():
        print(f"\n  In '{book_name}':")
        for contact in contacts:
            print(f"    - {contact}")
