from contacts import Contact


class AddressBook:
    """Manages a collection of contacts."""
    
    def __init__(self, name):
        self.name = name
        self.contacts = []
        
    def add_contact(self, contact):
        """Add a contact to the address book."""
        if contact in self.contacts:
            print(f"Contact {contact.first_name} {contact.last_name} already exists.")
            return False
        self.contacts.append(contact)
        print(f"Contact {contact.first_name} {contact.last_name} added.")
        return True
    
    def remove_contact(self, contact):
        """Remove a contact from the address book."""
        if contact in self.contacts:
            self.contacts.remove(contact)
            print(f"Contact {contact.first_name} {contact.last_name} removed.")
            return True
        print(f"Contact {contact.first_name} {contact.last_name} not found.")
        return False
        
    def edit_contact(self, old_contact, new_contact):
        """Edit an existing contact."""
        if old_contact in self.contacts:
            index = self.contacts.index(old_contact)
            self.contacts[index] = new_contact
            print(f"Contact {old_contact.first_name} {old_contact.last_name} updated.")
            return True
        print(f"Contact {old_contact.first_name} {old_contact.last_name} not found.")
        return False
            
    def display_contacts(self):
        """Display all contacts in the address book."""
        if not self.contacts:
            print(f"Address Book '{self.name}' is empty.")
            return
        print(f"\n=== Address Book: {self.name} ===")
        for contact in self.contacts:
            print(f"  {contact}")
    
    def get_contact_count(self):
        """Return the number of contacts."""
        return len(self.contacts)

