def printTicket(name,age1,dob):
    print("**********************")
    print("Welcome to JetAirways")
    print("**********************")
    print("Ticket Number:",age1*4)
    print("Name:",name)
    print("Age:",age1)
    print("dob:",dob)
    print("**********************")

def buyTicket():
    name = input("Enter your name:")
    age = input("Enter your age:")
    dob = input("Enter your dob:")
    printTicket(name,age,dob)

for i in range(2):
    buyTicket()