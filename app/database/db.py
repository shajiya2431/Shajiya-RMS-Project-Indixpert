# import json
# from app.logs.logger import Logger

# USER_FILE = "app/database/user.json"
# MENU_FILE = "app/database/menu.json"
# ORDER_FILE = "app/database/order_history.json"
# BILL_FILE = "app/database/bill_history.json"
# TABLE_FILE = "app/database/table.json"


# class Database:

#     # ================= USERS =================

#     def read_data(self):
#         try:
#             with open(USER_FILE, "r") as file:
#                 data = json.load(file)
#                 Logger.log("Users Read")
#                 return data
#         except:
#             Logger.log("Users File Empty or Not Found")
#             return []

#     def write_users(self, data):
#         with open(USER_FILE, "w") as file:
#             json.dump(data, file, indent=4)
#         Logger.log("Users Saved")

#     def add_user(self, user):
#         data = self.read_data()
#         data.append(user)
#         self.write_users(data)
#         Logger.log(f"User Added - {user['username']}")

#     def get_all_users(self):
#         return self.read_data()


#     # ================= MENU =================

#     def read_menu(self):
#         try:
#             with open(MENU_FILE, "r") as file:
#                 data = json.load(file)
#                 Logger.log("Menu Read")
#                 return data
#         except:
#             Logger.log("Menu File Empty")
#             return {}

#     def write_menu(self, data):
#         with open(MENU_FILE, "w") as file:
#             json.dump(data, file, indent=4)
#         Logger.log("Menu Saved")

#     def get_menu(self):
#         return self.read_menu()



#     def read_orders(self):
#         try:
#             with open(ORDER_FILE, "r") as file:
#                 data = json.load(file)
#                 Logger.log("Orders Read")
#                 return data
#         except:
#             Logger.log("Orders File Empty")
#             return []

#     def write_orders(self, data):
#         with open(ORDER_FILE, "w") as file:
#             json.dump(data, file, indent=4)
#         Logger.log("Orders Saved")

#     def add_order(self, order):
#         data = self.read_orders()
#         data.append(order)
#         self.write_orders(data)
#         Logger.log("Order Added")


#     # ================= BILLS =================

#     def read_bills(self):
#         try:
#             with open(BILL_FILE, "r") as file:
#                 data = json.load(file)
#                 Logger.log("Bills Read")
#                 return data
#         except:
#             Logger.log("Bills File Empty")
#             return []

#     def write_bills(self, data):
#         with open(BILL_FILE, "w") as file:
#             json.dump(data, file, indent=4)
#         Logger.log("Bills Saved")

#     def add_bill(self, bill):
#         data = self.read_bills()
#         data.append(bill)
#         self.write_bills(data)
#         Logger.log(f"Bill Added - {bill['bill_no']}")

#     TABLE_FILE = "app/database/table.json"


# # ================= TABLE =================

#     def read_tables(self):
#         try:
#             with open(TABLE_FILE, "r") as file:
#                 data = json.load(file)
#                 Logger.log("Tables Read")
#                 return data
#         except:
#             Logger.log("Table File Empty")
#             return []

#     def write_tables(self, data):
#         with open(TABLE_FILE, "w") as file:
#             json.dump(data, file, indent=4)
#         Logger.log("Tables Saved")

#     def add_table(self, table):
#         data = self.read_tables()
#         data.append(table)
#         self.write_tables(data)
#         Logger.log(f"Table Booked - {table['table_no']}")





import json
from app.logs.logger import Logger

USER_FILE = "app/database/user.json"
MENU_FILE = "app/database/menu.json"
ORDER_FILE = "app/database/order_history.json"
BILL_FILE = "app/database/bill_history.json"
TABLE_FILE = "app/database/table.json"


class Database:

    

    def read_data(self):
        try:
            with open(USER_FILE, "r") as file:
                data = json.load(file)
                Logger.log("Users Read")
                return data
        except:
            Logger.log("Users File Empty or Not Found")
            return []

    def write_users(self, data):
        with open(USER_FILE, "w") as file:
            json.dump(data, file, indent=4)
        Logger.log("Users Saved")

    def add_user(self, user):
        data = self.read_data()
        data.append(user)
        self.write_users(data)
        Logger.log(f"User Added - {user['username']}")

    def get_all_users(self):
        return self.read_data()


    

    def read_menu(self):
        try:
            with open(MENU_FILE, "r") as file:
                data = json.load(file)
                Logger.log("Menu Read")
                return data
        except:
            Logger.log("Menu File Empty")
            return {}

    def write_menu(self, data):
        with open(MENU_FILE, "w") as file:
            json.dump(data, file, indent=4)
        Logger.log("Menu Saved")

    def get_menu(self):
        return self.read_menu()


    

    def read_orders(self):
        try:
            with open(ORDER_FILE, "r") as file:
                data = json.load(file)
                Logger.log("Orders Read")
                return data
        except:
            Logger.log("Orders File Empty")
            return []

    def write_orders(self, data):
        with open(ORDER_FILE, "w") as file:
            json.dump(data, file, indent=4)
        Logger.log("Orders Saved")

    def add_order(self, order):
        data = self.read_orders()
        data.append(order)
        self.write_orders(data)
        Logger.log("Order Added")


    

    def read_bills(self):
        try:
            with open(BILL_FILE, "r") as file:
                data = json.load(file)
                Logger.log("Bills Read")
                return data
        except:
            Logger.log("Bills File Empty")
            return []

    def write_bills(self, data):
        with open(BILL_FILE, "w") as file:
            json.dump(data, file, indent=4)
        Logger.log("Bills Saved")

    def add_bill(self, bill):
        data = self.read_bills()
        data.append(bill)
        self.write_bills(data)
        Logger.log(f"Bill Added - {bill['bill_no']}")


    # ================= TABLE =================

    def read_tables(self):
        try:
            with open(TABLE_FILE, "r") as file:
                data = json.load(file)
                Logger.log("Tables Read")
                return data
        except:
            Logger.log("Table File Empty")
            return []

    def write_tables(self, data):
        with open(TABLE_FILE, "w") as file:
            json.dump(data, file, indent=4)
        Logger.log("Tables Saved")

    def add_table(self, table):
        data = self.read_tables()
        data.append(table)
        self.write_tables(data)
        Logger.log(f"Table Booked - {table['table_no']}")