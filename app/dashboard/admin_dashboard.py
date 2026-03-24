from app.database.db import Database
from app.menu.view_menu import ViewMenu
class AdminDashboard:

    def __init__(self):
        self.db = Database()

    def menu(self):
        while True:
            print("\n====== ADMIN PANEL ======")
            print("1. View Menu")
            print("2. Add Item")
            print("3. Delete item")
            print("4. Update Item")
            print("5. Logout")

            choice = input("Enter Choice: ")

            if choice == "1":
                ViewMenu(self.db).show()
                data = self.db.read_data()
                menu = data.get("menu", [])

                print("\nID     |       Category    |   Half    |   Full")
                print("-" * 50)

                for item in menu:
                    print(f"{item['id']}  | {item['name']} | {item['category']} | ₹{item['half_price']} | ₹{item['full_price']}")

            elif choice == "2":
                data = self.db.read_data()

                item = {
                    "id": input("Enter Item ID: "),
                    "name": input("Enter Item Name: "),
                    "category": input("Enter Category: "),
                    "half_price": int(input("Enter Half Price: ")),
                    "full_price": int(input("Enter Full Price: "))
                }

                data["menu"].append(item)
                self.db.write_data(data)

                print("Item Added")

            elif choice == "3":
                data = self.db.read_data()
                item_id = input("Enter Item ID to delete: ")

                data["menu"] = [i for i in data["menu"] if i["id"] != item_id]

                self.db.write_data(data)
                print("Item Deleted")

            elif choice == "4":
                data = self.db.read_data()
                item_id = input("Enter Item ID to Update: ")

                found = False

                for item in data["menu"]:
                    if item["id"] == item_id:
                        found = True
                        item["name"] = input("New Name: ")
                        item["category"] = input("New Half Price: ")
                        item["half_price"] = int(input("New Full Price: "))
                        item["full_price"] = int(input("New Full Price: "))

                self.db.write_data(data)

                if found:
                    print("Item Updated")
                else:
                    print("Item not found")

            elif choice == "5":
                print("Logout")
                break
            else:
                print("Invalid Choice")
