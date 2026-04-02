from app.database.db import Database
from app.menu.view_menu import ViewMenu
from app.order.take_order import TakeOrder
from app.order.view_order import ViewOrders
from app.booking.table_booking import TableBooking
from app.billing.bill import GenerateBill
from app.menu.search_item import SearchItem
from app.logs.logger import Logger


class StaffDashboard:

    def __init__(self):
        self.db = Database()

    def menu(self):

        Logger.log("Staff Dashboard Opened")

        while True:

            print("\n====== STAFF DASHBOARD ======")
            print("1. View Menu")
            print("2. Search Item")
            print("3. Take Order")
            print("4. View Orders")
            print("5. Table Booking")
            print("6. Generate Bill")
            print("7. Logout")

            choice = input("Enter Choice: ")

            if choice == "1":
                Logger.log("Staff Clicked View Menu")
                ViewMenu(self.db).show()

            elif choice == "2":
                Logger.log("Staff Clicked Search Item")
                SearchItem(self.db).search()
                

            elif choice == "3":
                Logger.log("Staff Clicked Take Order")
                TakeOrder(self.db).take()

            elif choice == "4":
                Logger.log("Staff Clicked View Orders")
                ViewOrders(self.db).show()

            elif choice == "5":
                Logger.log("Staff Clicked Table Booking")
                TableBooking(self.db).book()

            elif choice == "6":
                Logger.log("Staff Clicked Generate Bill")
                GenerateBill(self.db).bill()

            elif choice == "7":
                Logger.log("Staff Logout")
                print("Logout Successfully")
                break

            else:
                print("Invalid Choice")
                Logger.log("Staff Entered Invalid Choice")