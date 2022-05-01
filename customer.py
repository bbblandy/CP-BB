class Customer:

    def __init__(self, email='na', firstName='na', lastName='na'):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName

    # getters or accessors provide access to each attribute
    @property
    def getEmail(self):
        return self.__email

    @property
    def getFirstName(self):
        return self.__firstName

    @property
    def getLastName(self):
        return self.__lastName

   # setters or mutators allow a programmer to change attribute value

    @email.setter
    def setEmail(self, email):
        self.__email = email


    def setFirstName(self, firstName):
        self.__firstName = firstName


    def setLastName(self, lastName):
        self.__lastName = lastName

    def __str__(self):
        return f'Customer(first: {self.firstName}, last: {self.lastName}, email: {self.email})'

