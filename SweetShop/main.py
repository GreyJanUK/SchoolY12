# Your program should show your programming skills, it should:
# Allow the User to login
# Display a menu
# Allow the user to pick a sweet from the menu
# Allow the user to enter a number of 100g bags
# Allow the user to preview the price before adding to a ‘Shopping Basket’
# Allow the user to continue adding to the ‘Shopping Basket’ until they are happy with their order. If duplicate items are entered, the count of the item should increase rather than duplicating another entry for the same item.
# Allow the user to view their ‘Basket’ and either Continue Shopping or Checkout
# Display the contents and cost of the items in the Basket - with VAT of 20% if you wish
# Allow the user to remove basket contents fully/partially before checkout.
# Remove a discount of 10% of orders over £15
# Remove a discount of 12% of orders over £25
# Remove a discount of 20% of orders over £40 and give free shipping.
# Shipping costs are at a flat cost of £5.99 - this is not included in the discount.

import getpass
import pyinputplus as pyi

itemList = []
shoppingList = []
accountDict = {}
running = False

def ImportItems():
    file = open("sweets.txt","r")
    for line in file:
        print(line)

def updateAccounts(arg1,arg2):
    a = arg1
    b = arg2
    if a == 0 and b == 0:
        file = open("accounts.txt","r")
        for x in file:
            (key, val) = x.split()
            accountDict[str(key)] = val
        file.close()
    else:
        file = open("accounts.txt","a")
        file.write("\n{0} {1}".format(arg1, arg2))
        print(accountDict)

updateAccounts(0,0) # Sending this function 0,0 will update the cached list of accounts rather than adding a new account- still need to add a check to make sure the user doesnt enter 0,0 though

def add_user(accountDict):
    user = input("Create a Username: ")
    password = getpass.getpass("Enter a password: ")
    for key in accountDict:
        if user == key:
            print("That user is already in use!", accountDict) # add an aditional check to make sure they don't try 0,0
            return False
    else:
        updateAccounts(user, password)
        return True

def log_in():
    user = input("Enter username: ")
    password = getpass.getpass("Enter a password: ")
    if validateLogin(user, password, accountDict):
        return True

def validateLogin(user, password, accountDict): # could make this nested
    if accountDict.get(user)== password:
        return True
    else:
        return False

def Initial(): # Run this when the program first runs 
    a = int(input("Welcome to the shop, would you like to:\n1) Log in\n2) Create a new account\nPlease enter a number: "))
    if a == 1:
        if log_in():
            running = True
    else:
        add_user(accountDict)
        b = str("Would you like to log in now?").lower()
        if b == "yes":
            if log_in():
                running = True
        else:
            print("Goodbye!")

def Add_to_Cart(item,qty): # add items to cart as either an array or a dict
    a = item
    b = qty

def CalculateTotal(cart): # cart will probably be a 2d table or a dictionary, depending on how I implement the rest of the functions 
    a = cart

def Browse(): # Print the cached table itemList
    print(itemList)
    


while running == True:
    a = pyi.inputChoice("Welcome to the shop!\nWould you like to:\nBrowse\nCheckout\nViewCart\nLogOut").lower()
    if a == "Browse":
        Browse()
    elif a == "Checkout":
        CalculateTotal(shoppingList)
    elif a == "viewCart":
        print(shoppingList)
    elif a == "LogOut":
        running = False
    



