








# from datetime import datetime, timedelta
# from app.logs.logger import Logger


# class TableBooking:

#     def __init__(self, db):
#         self.db = db

#     def book(self):

#         print("\n===== TABLE BOOKING =====")

#         # Restaurant me 10 tables assume kar rahe
#         total_tables = [1,2,3,4,5,6,7,8,9,10]

#         booked_tables = self.db.read_tables()

#         print("\n===== TABLE STATUS =====")

#         for table in total_tables:

#             booked = False

#             for b in booked_tables:
#                 if b["table_no"] == table:
#                     booked = True
#                     print(f"Table {table} : Booked ({b['start']} - {b['end']})")

#             if not booked:
#                 print(f"Table {table} : Available")

#         try:
#             table_no = int(input("\nEnter Table Number: "))
#         except:
#             print("Invalid Table Number")
#             return

#         # Check already booked
#         for table in booked_tables:
#             if table["table_no"] == table_no:
#                 print("Table Already Booked")
#                 Logger.log("Table Booking Failed - Already booked")
#                 return

#         # Booking Details
#         customer = input("Customer Name: ")
#         persons = input("No. of Persons: ")
#         phone = input("Phone Number: ")

#         start_time = input("Start Time (HH:MM): ")
#         duration = input("Duration (Hours): ")

#         try:
#             start = datetime.strptime(start_time, "%H:%M")
#             end = start + timedelta(hours=int(duration))
#         except:
#             print("Invalid Time Format")
#             return

#         table_data = {
#             "table_no": table_no,
#             "customer": customer,
#             "persons": persons,
#             "phone": phone,
#             "start": start.strftime("%H:%M"),
#             "end": end.strftime("%H:%M")
#         }

#         self.db.add_table(table_data)

#         print("\nTable Booked Successfully")
#         print(f"Table : {table_no}")
#         print(f"Customer : {customer}")
#         print(f"Persons : {persons}")
#         print(f"Phone : {phone}")
#         print(f"Time : {start.strftime('%H:%M')} - {end.strftime('%H:%M')}")

#         Logger.log(f"Table Booked - {table_no}")










from datetime import datetime, timedelta
from app.logs.logger import Logger


class TableBooking:

    def __init__(self, db):
        self.db = db

    def book(self):

        print("\n===== TABLE BOOKING =====")

        # Table with seat capacity
        tables = {
            1: 2,
            2: 4,
            3: 4,
            4: 6,
            5: 6,
            6: 8,
            7: 2,
            8: 4,
            9: 6,
            10: 8
        }

        booked_tables = self.db.read_tables()

        print("\n===== TABLE STATUS =====")

        for table, seats in tables.items():

            booked = False

            for b in booked_tables:
                if b["table_no"] == table:
                    booked = True
                    print(f"Table {table} ({seats} seats) : Booked {b['start']} - {b['end']}")

            if not booked:
                print(f"Table {table} ({seats} seats) : Available")

        try:
            table_no = int(input("\nSelect Table Number: "))
        except:
            print("Invalid Table")
            return

        # Check booked
        for table in booked_tables:
            if table["table_no"] == table_no:
                print("Table Already Booked")
                return

        # Ask seats
        seats_needed = int(input("How many seats needed: "))

        if seats_needed > tables[table_no]:
            print("Seats not available on this table")
            return

        # Booking Details
        customer = input("Customer Name: ")
        persons = input("No. of Persons: ")
        phone = input("Phone Number: ")

        start_time = input("Start Time (HH:MM): ")
        duration = input("Duration (Hours): ")

        try:
            start = datetime.strptime(start_time, "%H:%M")
            end = start + timedelta(hours=int(duration))
        except:
            print("Invalid Time Format")
            return

        data = {
            "table_no": table_no,
            "customer": customer,
            "persons": persons,
            "phone": phone,
            "start": start.strftime("%H:%M"),
            "end": end.strftime("%H:%M")
        }

        self.db.add_table(data)

        print("\nTable Booked Successfully")
        print(f"Table : {table_no}")
        print(f"Seats : {seats_needed}")
        print(f"Customer : {customer}")
        print(f"Time : {start.strftime('%H:%M')} - {end.strftime('%H:%M')}")

        Logger.log(f"Table Booked - {table_no}")