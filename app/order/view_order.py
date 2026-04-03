from app.logs.logger import Logger


class ViewOrders:

    def __init__(self, db):
        self.db = db

    def show(self):

        orders = self.db.read_orders()

        
        if not orders:
            print("No Orders Found")
            Logger.log("View Orders - No Orders Found")
            return

        # View orders opened
        Logger.log("View Orders Opened")

        print("\n" + "="*60)
        print(" ============= ORDER LIST ============= ")
        print("="*60)

        order_no = 1

        for order in orders:

            print(f"\nOrder No : {order_no}")
            print("-"*60)
            print(f"{'Item':<20} {'Qty':<5} {'Type':<8} {'Price':<10} {'Total':<10}")
            print("-"*60)

            grand_total = 0

            for item in order:

                if isinstance(item, dict):

                    name = item.get("name", "")
                    qty = item.get("qty", "")
                    size = item.get("size", "")
                    price = item.get("price", 0)
                    total = item.get("total", 0)

                    print(f"{name:<20} {qty:<5} {size:<8} ₹{price:<10} ₹{total:<10}")

                    grand_total += total

            print("-"*60)
            print(f"Grand Total : ₹{grand_total}")

            order_no += 1

        print("\n" + "="*60)

        Logger.log("Orders Viewed Successfully")