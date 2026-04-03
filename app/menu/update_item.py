from app.logs.logger import Logger


class UpdateItem:

    def __init__(self, db):
        self.db = db

    def update(self):

        Logger.log("Update Item Opened")

        menu = self.db.get_menu()

        item_id = input("Enter Item ID to Update: ")

        # validation
        if not item_id.isdigit():
            print("Item ID must be number")
            Logger.log("Update Item Failed - Invalid ID")
            return

        item_id = int(item_id)

        found = False

        for category, items in menu.items():
            for item in items:

                if item["id"] == item_id:

                    Logger.log(f"Item Found For Update - ID {item_id}")

                    print("\nItem Found")
                    print("Leave blank to keep old value\n")

                    name = input(f"Enter New Name ({item['name']}): ")

                    if name:
                        item["name"] = name

                    # Double item
                    if item["type"] == "double":

                        half = input(f"Enter Half Price ({item['half']}): ")
                        full = input(f"Enter Full Price ({item['full']}): ")

                        if half:
                            if half.isdigit():
                                item["half"] = int(half)

                        if full:
                            if full.isdigit():
                                item["full"] = int(full)

                    # Single item
                    else:

                        price = input(f"Enter Price ({item['price']}): ")

                        if price:
                            if price.isdigit():
                                item["price"] = int(price)

                    found = True
                    print("Item Updated Successfully")

                    Logger.log(f"Item Updated - ID {item_id} Name {item['name']}")

        if not found:
            print("Item not found")
            Logger.log(f"Update Failed - ID {item_id} Not Found")

        self.db.write_menu(menu)