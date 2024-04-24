import sqlite3
import sys

class Inventory:
    def __init__(self, database_name="methods.db"):
        self.database_name = database_name

    def viewInventory(self):
        """ Displays all inventory items. """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute("SELECT ISBN, Title, Author, Genre, Pages, ReleaseDate, Price, Stock FROM Inventory")
            rows = cursor.fetchall()
            print("Inventory List:")
            for row in rows:
                print(f"ISBN: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}, Pages: {row[4]}, Release: {row[5]}, Price: ${row[6]}, Stock: {row[7]}")
            cursor.close()
        except sqlite3.Error as e:
            print("Error fetching inventory:", e)
            sys.exit()
        finally:
            conn.close()

    def searchInventory(self, title):
        """ Searches for inventory items by title. """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute("SELECT ISBN, Title, Author, Stock FROM Inventory WHERE Title LIKE ?", ('%' + title + '%',))
            results = cursor.fetchall()
            if results:
                print("Search Results:")
                for result in results:
                    print(f"ISBN: {result[0]}, Title: {result[1]}, Author: {result[2]}, Stock: {result[3]}")
            else:
                print("No results found.")
            cursor.close()
        except sqlite3.Error as e:
            print("Search error:", e)
            sys.exit()
        finally:
            conn.close()

    def decreaseStock(self, ISBN, quantity=1):
        """ Decreases the stock for a specific ISBN. """
        try:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute("UPDATE Inventory SET Stock = Stock - ? WHERE ISBN = ? AND Stock >= ?", (quantity, ISBN, quantity))
            if cursor.rowcount == 0:
                print("Stock decrease failed: ISBN not found or insufficient stock.")
            else:
                print(f"Stock decreased for ISBN: {ISBN}")
                conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print("Error updating stock:", e)
            sys.exit()
        finally:
            conn.close()
