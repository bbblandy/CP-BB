from customer import *

def testConstructor():
    c1 = Customer()
    print(f"Testing constructor with default values.  Expect default values. {c1}")
    c2 = Customer('@', 'Brendan', 'Blandy')
    print(f"Testing constructor with parameters.  Expect customer Brendan. {c2}")


def testPropertyGetters():
    c = Customer('@', 'Brendan', 'Blandy')
    print(f"Testing property getters.  Expect individual attributes for person C.")
    print(f"Results -first: {c.firstName}, last: {c.lastName}, email: {c.email}")

def testPropertySetters():
    c = Customer('email', 'first', 'last')
    c.email= '@'
    c.firstName = "FIRST"
    c.lastName = "LAST"
    print(f"Testing property setters. Expect individual attributes for C to change. {c}")

#
# def testPropertySettersWithValidation():
#
#
#
# def testEncapsulation():





