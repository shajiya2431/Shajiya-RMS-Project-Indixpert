from app.logs.logger import Logger


class SalesReport:

    def __init__(self, db):
        self.db = db

    def report(self):

        Logger.log("Sales Report Opened")

        bills = self.db.read_bills()

        if not bills:
            print("No Sales Found")
            Logger.log("Sales Report Failed - No Sales Found")
            return

        print("\n" + "="*70)
        print("SALES REPORT")
        print("="*70)

        print(f"{'Bill No':<10}{'Table':<8}{'Date':<12}{'Payment':<10}{'Total':<10}")
        print("-"*70)

        total_sales = 0
        cash = 0
        upi = 0
        card = 0

        for bill in bills:

            print(
                f"{bill['bill_no']:<10}"
                f"{bill['table']:<8}"
                f"{bill['date']:<12}"
                f"{bill['payment']:<10}"
                f"₹{bill['total']:<10}"
            )

            total_sales += bill["total"]

            if bill["payment"] == "Cash":
                cash += bill["total"]

            elif bill["payment"] == "UPI":
                upi += bill["total"]

            elif bill["payment"] == "Card":
                card += bill["total"]

        print("-"*70)
        print(f"Total Sales : ₹{total_sales}")

        print("\nPayment Summary")
        print("-"*30)
        print(f"Cash : ₹{cash}")
        print(f"UPI  : ₹{upi}")
        print(f"Card : ₹{card}")

        print("="*70)

        Logger.log(f"Sales Report Generated - Total ₹{total_sales}")