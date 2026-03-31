from app.logs.logger import Logger

class TableBooking:

    tables = {}

    def __init__(self):
        pass

    def book(self):

        table_no = input("Enter Table Number: ")

        
        if table_no == "":
            print("Table number required")
            Logger.log("Table Booking Failed - Empty Table Number")
            return

        if table_no in TableBooking.tables:
            print("Table Already Booked")
            Logger.log(f"Table Booking Failed - Table {table_no} Already Booked")
            return

        name = input("Enter Customer Name: ")

        if name == "":
            print("Customer name required")
            Logger.log("Table Booking Failed - Empty Name")
            return

        people = input("Number of People: ")

        if not people.isdigit():
            print("People must be number")
            Logger.log("Table Booking Failed - Invalid People")
            return

        TableBooking.tables[table_no] = {
            "name": name,
            "people": people
        }

        print("Table Booked Successfully")

        Logger.log(f"Table Booked - Table {table_no} Name {name} People {people}")


    def view(self):

        if not TableBooking.tables:
            print("No Table Booked")
            Logger.log("View Table - No Booking Found")
            return

        Logger.log("View Table Booking Opened")

        print("\n")
        print("=" * 50)
        print("🍽️ TABLE BOOKINGS")
        print("=" * 50)

        print(f"{'TABLE':<10}{'NAME':<20}{'PEOPLE':<10}")
        print("-" * 50)

        for table, info in TableBooking.tables.items():
            print(f"{table:<10}{info['name']:<20}{info['people']:<10}")

        Logger.log("Table Booking Viewed")