from user import *
from cart import *
from inventory import *
from history import *


## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes
    user = User()
    cart = Cart()
    inventory = Inventory()
    history = OrderHistory()

    ## initial menu
    while(1):
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if(initial == "0"):
            user.login()

        elif(initial == "1"):
            user.createAccount()

        ## exit program
        elif(initial == "2"):
            print("Good-bye!")
            break

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

        ## checks status after one menu loop...
        ## goes into main menu if applicable
        if(user.getLoggedIn()):
            mainMenu(user, cart, inventory, history)


## incomplete main menu...
def mainMenu(user, cart, inventory, history):
    while(user.getLoggedIn()):
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")
        print("3. Cart Information")
        print("4. Order Information")
        option = input("Enter your menu choice: ")
        print()

        if option == "0":
            user.logout()
            print("Successful logout.")
            break

        elif option == "1":
            user.viewAccountInformation()

        elif option == "2":
            inventoryMenu(inventory)

        elif option == "3":
            cartMenu(cart, user)

        elif option == "4":
            orderHistoryMenu(history, user)

        else:
            print("That's not a menu option. Please try again.")

        print()

def inventoryMenu(inventory):
    while True:
        print("Inventory Information:")
        print("0. Go Back")
        print("1. View Inventory")
        print("2. Search Inventory")
        choice = input("Enter your inventory choice: ")
        if choice == "0":
            break
        elif choice == "1":
            inventory.viewInventory()
        elif choice == "2":
            title = input("Enter the title to search: ")
            inventory.searchInventory(title)
        else:
            print("Invalid choice, please try again.")

def cartMenu(cart, user):
    while True:
        print("Cart Information:")
        print("0. Go Back")
        print("1. View Cart")
        print("2. Add Items to Cart")
        print("3. Remove an Item from Cart")
        print("4. Check Out")
        choice = input("Enter your cart choice: ")
        if choice == "0":
            break
        elif choice == "1":
            cart.viewCart(user.getUserID())
        elif choice == "2":
            ISBN = input("Enter ISBN of the book to add: ")
            quantity = int(input("Enter quantity: "))
            cart.addToCart(user.getUserID(), ISBN, quantity)
        elif choice == "3":
            ISBN = input("Enter ISBN of the book to remove: ")
            cart.removeFromCart(user.getUserID(), ISBN)
        elif choice == "4":
            cart.checkOut(user.getUserID())
        else:
            print("Invalid choice, please try again.")

def orderHistoryMenu(history, user):
    while True:
        print("Order History Information:")
        print("0. Go Back")
        print("1. View Order History")
        print("2. View Order")
        choice = input("Enter your order choice: ")
        if choice == "0":
            break
        elif choice == "1":
            history.viewHistory(user.getUserID())
        elif choice == "2":
            orderID = input("Enter the order ID: ")
            history.viewOrder(user.getUserID(), orderID)
        else:
            print("Invalid choice, please try again.")

def main():
    print("Welcome to the online bookstore!\n")
    initialMenu()

main()

