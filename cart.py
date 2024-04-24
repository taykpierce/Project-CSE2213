import sqlite3
import sys

class Cart:
    def __init__(self, database_name="methods.db"):
        self.database_name = database_name

    def addToCart(self, userID, ISBN, quantity=1):
        """ Adds a specified quantity of an item to the user's cart. """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            # Check if the item already exists in the cart
            cursor.execute("SELECT Quantity FROM Cart WHERE UserID=? AND ISBN=?", (userID, ISBN))
            result = cursor.fetchone()
            if result:
                new_quantity = result[0] + quantity
                cursor.execute("UPDATE Cart SET Quantity=? WHERE UserID=? AND ISBN=?", (new_quantity, userID, ISBN))
            else:
                cursor.execute("INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (?, ?, ?)", (userID, ISBN, quantity))
            conn.commit()
            print("Item added to cart.")
            cursor.close()
        except sqlite3.Error as e:
            print("Failed to add item to cart:", e)
            sys.exit()
        finally:
            conn.close()

    def viewCart(self, userID):
        """ Displays all items currently in the user's cart. """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute("SELECT Cart.ISBN, Inventory.Title, Cart.Quantity FROM Cart JOIN Inventory ON Cart.ISBN = Inventory.ISBN WHERE Cart.UserID=?", (userID,))
            items = cursor.fetchall()
            if items:
                print("Items in your cart:")
                for item in items:
                    print(f"ISBN: {item[0]}, Title: {item[1]}, Quantity: {item[2]}")
            else:
                print("Your cart is empty.")
            cursor.close()
        except sqlite3.Error as e:
            print("Failed to retrieve cart items:", e)
            sys.exit()
        finally:
            conn.close()

    def removeFromCart(self, userID, ISBN):
        """ Removes an item from the user's cart. """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Cart WHERE UserID=? AND ISBN=?", (userID, ISBN))
            conn.commit()
            if cursor.rowcount == 0:
                print("No such item in cart.")
            else:
                print("Item removed from cart.")
            cursor.close()
        except sqlite3.Error as e:
            print("Failed to remove item from cart:", e)
            sys.exit()
        finally:
            conn.close()
