import random
from datetime import datetime
from app.logs.logger import Logger

class GenerateBill:

    def __init__(self, db):
        self.db = db

    def bill(self):

        orders = self.db.read_orders()

        if not orders:
            print("No Orders Found")
            Logger.log("Generate Bill Failed - No Orders")
            return
        
        table = input ("Enter Table Number: ")

        if table == "":
            print("Table number required")
            Logger.log("Generate Bill Failed - Empty Table")
            return 
        
        bill_no = random.randint(1000,9999)

        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        print("\n" + "="*75)
        print("🍽️            INVOICE / FINAL BILL             🍽️")
        print("="*75)

        print(f"Bill No    : {bill_no}")
        print(f"Table No   : {table}")
        print(f"Date       : {date}")
        print(f"Time       : {time}")

        print("-"*75)
        print(f"{'NO':<5}{'ITEM':<25}{'QTY':<8}{'TYPE':<10}{'TOTAL':<10}")
        print("-"*75)

        grand_total = 0
        no = 1

        last_order = orders[-1]

        for item in last_order:
             
            name = item.get("name")
            qty = item.get("qty")
            size = item.get("size")
            total = item.get("total")

            print(f"{no:<5}{name:<25}{qty:<8}{size:<10}₹{total:<10}")

            grand_total += total
            no += 1

        print("-"*75)

        cgst = grand_total * 0.025
        sgst = grand_total * 0.025
        service = grand_total * 0.10

        final_total = grand_total + cgst + sgst + service

        print(f"Sub Total       : ₹{grand_total}")
        print(f"CGST (2.5%)     : ₹{cgst:.2f}")
        print(f"SGST (2.5%)     : ₹{sgst:.2f}")
        print(f"Service (10%)   : ₹{service:.2f}")

        print("-"*75)
        print(f"Final Total     : ₹{final_total:.2f}")

        print("-"*75)

        print("\nSelect Payment Mode")
        print("1. Cash")
        print("2. UPI")
        print("3. Card")

        choice = input("Enter Payment Mode: ")

        if choice == "1":
            payment = "Cash"
        elif choice == "2":
            payment = "UPI"
        elif choice == "3":
            payment = "Card"
        else:
            payment = "Unknown"

        print(f"Payment Mode : {payment}")


        print("="*75)
        print("Thank You Visit Again")
        print("="*75)

        
        Logger.log(f"Bill Generated - Bill No {bill_no} Table {table} Total ₹{final_total} Payment {payment}")

        bill_data = {
            "bill_no": bill_no,
            "table": table,
            "date": date,
            "time": time,
            "total": final_total,
            "payment": payment
        }

        self.db.add_bill(bill_data)

        Logger.log(f"Bill Saved - {bill_no}")