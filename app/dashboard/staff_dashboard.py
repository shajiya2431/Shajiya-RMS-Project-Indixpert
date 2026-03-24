from app.database.db import Database
from app.menu.view_menu import ViewMenu

class StaffDashboard:

    def __init__(self):
        self.db = Database()
        self.orders = []
        self.tables = []

    def menu(self):
        while True:
            print("\n====== STAFF DASHBOARD ======")
            print("1. View Menu")
            print("2. Take Order")
            print("3. View Orders")
            print("4. Table Booking")
            print("5. Generate Bill")
            print("6. Logout")

            choice = input("Enter Choice: ")

            if choice == "1":
                ViewMenu(self.db).show()

            elif choice == "2":
                menu = self.db.get_menu()

                item_id = input("Enter Item Id: ")
                quantity = int(input("Enter Quantity: "))
                plate = input("Half / Full: ").lower()

                found = False

                for category, items in menu.items():
                    for item in items:
                        if item["id"] == item_id:
                            found = True

                            if plate == "half":
                                price = item["half_price"]
                            elif plate == "full":
                                price = item["full_price"]
                            else:
                                print("Invalid plate type ❌")
                                break

                            total = price * quantity

                            order = {
                                "name": item["name"],
                                "quantity": quantity,
                                "type": plate,
                                "price": total
                            }

                            self.orders.append(order)
                            print("Order Added")
                
                if not found:
                    print("Item not found")

            elif choice == "3":
                print("\n------ ORDERS ------")
                for i, order in enumerate(self.orders, start =1):
                    print(f"{i}. {order['name']} | Qty:{order['quantity']} | {order['type']} | ₹{order['total']}")

                if not self.orders:
                    print("No Orders")

                
            elif choice == "4":
                table_no = input("Enter Table Number: ")
                name = input("Enter Customer Name: ")

                self.tables[table_no] == name
                print(f"Table {table_no} booked for {name}")

            elif choice == "5":
                if not self.orders:
                    print("No orders to bill")
                    continue

                print("\n====== FINAL BILL ======")

                grand_total = 0

                for order in self.orders:
                    print(f"{order['name']} | {order['quantity']} | ₹{order['total']}")
                    grand_total += order["total"]

                print("-------------------------")
                print("TOTAL BILL:", grand_total, "₹")
                print("=========================")

                self.orders.clear()

            elif choice == "6":
                print("Logout.....")
                break
            else:
                print("Invalid Choice")
                
