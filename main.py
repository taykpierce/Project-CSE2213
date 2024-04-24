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

        ## logging out
        if(option == "0"):
            user.logout()

            print("Successful logout.")
            break 

        elif option == "1":
            user.viewAccountInformation()
        
        elif option == "2":
            print ("Inventory Menu:")
            print ("a. View Inventory")
            print ("b. Search Inventory")
            inventory_option = input("Enter your inventory choice: ")

            if inventory_option == "a":
                inventory.viewInventory()
            elif inventory_option == "b":
                title = input("Enter the title to search: ")
                inventory.searchInventory(title)
            
            else:
                print("That not a valid")

        elif option == "3":
            print("Cart Menu:")
            print("a. View Cart")
            print("b. Add Item to Cart")
            print("c. Remove Item from Cart")
            cart_option = input("Enter your cart choice: ")

            if cart_option == "a":
                cart.viewCart(user.getUserID())
            
            elif cart_option == "b":
                orderID = 


        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()


def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
