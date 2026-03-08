from address_book import AddressBook


class AddressBookSystem:
    """Manages multiple address books."""
    
    def __init__(self):
        self.address_books = {}
        
    def create_address_book(self, name):
        """Create a new address book with the given name."""
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
            return None
        self.address_books[name] = AddressBook(name)
        print(f"Address book '{name}' created.")
        return self.address_books[name]
    
    def get_address_book(self, name):
        """Get an address book by name."""
        return self.address_books.get(name, None)
    
    def delete_address_book(self, name):
        """Delete an address book by name."""
        if name in self.address_books:
            del self.address_books[name]
            print(f"Address book '{name}' deleted.")
            return True
        print(f"Address book '{name}' not found.")
        return False
    
    def list_address_books(self):
        """List all address book names."""
        return list(self.address_books.keys())
    
    def display_all_address_books(self):
        """Display all address books and their contacts."""
        if not self.address_books:
            print("No address books available.")
            return
        for address_book in self.address_books.values():
            address_book.display_contacts()
