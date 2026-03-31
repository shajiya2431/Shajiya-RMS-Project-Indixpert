from app.database.db import Database
from app.menu.view_menu import ViewMenu
from app.menu.add_item import AddItem
from app.menu.update_item import UpdateItem
from app.menu.delete_item import DeleteItem
from app.order.view_order import ViewOrders
from app.report.sales_report import SalesReport
from app.logs.logger import Logger



class AdminDashboard:
    
    def __init__(self):
        self.db = Database()

    def menu(self):

        Logger.log("Admin Dashboard Opened")

        while True:

            print("\n====== ADMIN DASHBOARD ======")
            print("1. View Menu")
            print("2. Add Item")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. View Orders")
            print("6. Sales Report")
            print("7. Logout")

            choice = input("Enter Choice: ")

            if choice == "1":
                Logger.log("Admin Clicked View Menu")
                ViewMenu(self.db).show()

            elif choice == "2":
                Logger.log("Admin Clicked Add Item")
                AddItem(self.db).add()

            elif choice == "3":
                Logger.log("Admin Clicked Update Item")
                UpdateItem(self.db).update()

            elif choice == "4":
                Logger.log("Admin Clicked Delete Item")
                DeleteItem(self.db).delete()

            elif choice == "5":
                Logger.log("Admin Clicked View Orders")
                ViewOrders(self.db).show()

            elif choice == "6":
                Logger.log("Admin Clicked Sales Report")
                SalesReport(self.db).report()
                
            elif choice == "7":
                Logger.log("Admin Logout")
                print("Logout Successfully")
                break

            else:
                print("Invalid Choice")
                Logger.log("Admin Entered Invalid Choice")