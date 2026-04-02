from app.logs.logger import Logger


class TakeOrder:

    def __init__(self, db):
        self.db = db

    def take(self):

        menu = self.db.get_menu()
        orders = []

        if not menu:
            print("Menu not available")
            Logger.log("Take Order Failed - Menu not available")
            return

        while True:

            try:
                item_id = int(input("Enter Item ID (0 to stop): "))
            except:
                print("Invalid ID")
                Logger.log("Invalid Item ID entered")
                continue

            if item_id == 0:
                break

            try:
                qty = int(input("Enter Quantity: "))

                # Quantity validation
                if qty <= 0 or qty > 20:
                    print("Invalid Quantity (1-20 allowed)")
                    Logger.log("Invalid Quantity Range")
                    continue

            except:
                print("Invalid Quantity")
                Logger.log("Invalid Quantity entered")
                continue

            size = input("Half / Full : ").lower()

            found = False

            for category, items in menu.items():
                for item in items:

                    if item["id"] == item_id:

                        if item["type"] == "double":

                            if size not in ["half", "full"]:
                                print("Invalid Size")
                                Logger.log("Invalid Size Selected")
                                continue

                            price = item[size]

                        else:
                            price = item["price"]
                            size = "single"

                        total = qty * price

                        orders.append({
                            "name": item["name"],
                            "qty": qty,
                            "size": size,
                            "price": price,
                            "total": total
                        })

                        print("Order Added")

                        Logger.log(f"Order Added - {item['name']} Qty {qty} {size}")

                        found = True

            if not found:
                print("Item not found")
                Logger.log(f"Item Not Found - ID {item_id}")

        if orders:
            self.db.add_order(orders)
            print("Order Saved Successfully")

            Logger.log("Order Saved Successfully")

        else:
            print("No order placed")
            Logger.log("No Order Placed")