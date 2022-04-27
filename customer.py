class Customer:
    # """ This class representa a customer.  It uses private attributes and property getters and setters.
    #     Setters have appropriate validation that raise an exception when invalid data is used."""
    #
    def __init__(self, email='na', firstName='na', lastName='na'):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName

    # getters or accessors provide access to each attribute
    @property
    def getEmail(self):
        return self.email

    @property
    def getFirstName(self):
        return self.firstName

    @property
    def getLastName(self):
        return self.lastName

   # setters or mutators allow a programmer to change attribute value

    #@email.setter
    def setEmail(self, email):
        self.email = email

    # @firstName.setter
    def setFirstName(self, firstName):
        self.firstName = firstName

    # @lastName.setter
    def setLastName(self, lastName):
        self.lastName = lastName

    def __str__(self):
    # """ another "magic method" that converts a product object into a string.
    #     When you call print(p) or print(str(p)) this method is called "under the covers" on your behalf"""
        return f'Customer(first: {self.firstName}, last: {self.lastName}, email: {self.email})'

