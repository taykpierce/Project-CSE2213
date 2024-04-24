import sqlite3
import sys
import random

class OrderHistory:
    def __init__(self, database_name="methods.db"):
        self.database_name = database_name

    def createOrder(self, userID, quantity, cost, date):
        """ Creates a new order entry in the Orders table with provided details. """
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                # Generate a unique order ID
                while True:
                    orderID = random.randint(100000, 999999)
                    cursor.execute("SELECT OrderID FROM Orders WHERE OrderID=?", (orderID,))
                    if not cursor.fetchone():
                        break
                cursor.execute("INSERT INTO Orders (OrderID, UserID, ItemNumber, Cost, Date) VALUES (?, ?, ?, ?, ?)", 
                               (orderID, userID, quantity, cost, date))
                conn.commit()
                print(f"New order created. Order ID: {orderID}")
                return orderID
        except sqlite3.Error as e:
            print("Failed to create an order:", e)
            sys.exit()

    def addOrderItems(self, orderID, items):
        """ Adds items to the specified order from the user's cart. """
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                for ISBN, quantity in items:  # items should be a list of tuples (ISBN, Quantity)
                    cursor.execute("INSERT INTO OrderItems (OrderID, ISBN, Quantity) VALUES (?, ?, ?)", 
                                   (orderID, ISBN, quantity))
                conn.commit()
                print(f"Items added to order {orderID}.")
                
        except sqlite3.Error as e:
            print("Failed to add items to the order:", e)
            sys.exit()

    def viewHistory(self, userID):
        """ Displays all past orders for a given user. """
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT OrderID, Date, Cost FROM Orders WHERE UserID=?", (userID,))
                orders = cursor.fetchall()
                print("Order History:")
                for order in orders:
                    print(f"Order ID: {order[0]}, Date: {order[1]}, Total Cost: ${order[2]}")
        except sqlite3.Error as e:
            print("Failed to retrieve order history:", e)
            sys.exit()

    def viewOrder(self, userID, orderID):
        """ Displays details of a specific order, confirming it belongs to the user. """
        try:
            with sqlite3.connect(self.database_name) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT UserID FROM Orders WHERE OrderID=?", (orderID,))
                if cursor.fetchone()[0] != userID:
                    print("This order does not belong to the current user.")
                    return
                cursor.execute("SELECT Inventory.ISBN, Inventory.Title, OrderItems.Quantity FROM OrderItems JOIN Inventory ON OrderItems.ISBN = Inventory.ISBN WHERE OrderItems.OrderID=?", (orderID,))
                items = cursor.fetchall()
                print(f"Details for Order {orderID}:")
                for item in items:
                    print(f"ISBN: {item[0]}, Title: {item[1]}, Quantity: {item[2]}")
        except sqlite3.Error as e:
            print("Failed to view order details:", e)
            sys.exit()
