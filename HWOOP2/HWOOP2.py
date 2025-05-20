class Customer:
    def __init__(self, name, email, id):
        print('New customer created!')
        self.name = name
        self.email = email
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        # Make sure the id is positive
        if value > 0:
            self.__id = value

    def __str__(self) -> str:
        return f"Customer '{self.name}' (ID: {self.__id}) - Email: {self.email} "

    def __repr__(self) -> str:
        return f"Customer(name='{self.name}', email='{self.email}', id='{self.__id}')"

    def __del__(self):
        print(f"Customer {self.name} is being removed!")

# Create 2 new customers
c1 = Customer("Alice", "alice@example.com", 101)
c2 = Customer("Bob", "bob@example.com", 202)

# Print both customers using print() and repr()
print(c1)
print(repr(c2))

# Trying to set an invalid id and verify if it was rejected
c1.id = -5
print(c1)
# The invalid id was rejected