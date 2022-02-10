"""The complete solution can be compiled by putting together all of
the code snippets from the steps of the example.The result is a program
that asks for the data from five customers and stores them in a list."""
class Customer:
    def __init__(self):
        self.name = None
        self.address = None
        self.phone = None
        self.balance = None
    def setName(self, name):
        self.name = name
    def setAddress(self, address):
        self.address = address
    def setPhone(self, phone):
        if len(phone) == 12:
            self.phone = phone
            return True
        else:
            print("Phone number must be ###-###-####")
            return False
    def setBalance(self, balance):
        if int(balance) > 0:
            self.balance = balance
            return True
        else:
            print("No negative balance is allowed.")
            return False
    def printCustomer(self):
        print(self.name,"at",self.address,"and phone number",self.phone,"owes $",self.balance)

customers = list()
for i in range(0,5):
    temp = Customer()
    temp.setName(input("Input Name:"))
    temp.setAddress(input("Input Address:"))
    while not temp.setPhone(input("Input Phone:")):
        print("Enter the phone again:")
    while not temp.setBalance(input("Input Balance:")):
        print("Enter the balance again:")
    customers.append(temp)

individual = input("What customer would you like to list?")
for i in range(0,5):
    if customers[i].name == individual:
        customers[i].printCustomer()     