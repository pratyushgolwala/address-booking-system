class Contact:
    """Represents a contact with personal information."""
    
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
        
    def __str__(self):
        return (f"{self.first_name} {self.last_name}, "
                f"{self.address}, {self.city}, "
                f"{self.state} - {self.zip_code}, "
                f"Phone: {self.phone_number}, Email: {self.email}")
    
    def __eq__(self, other):
        if isinstance(other, Contact):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name)
        return False
    
    def __hash__(self):
        return hash((self.first_name, self.last_name))
