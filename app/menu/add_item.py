from app.logs.logger import Logger


class AddItem:

    def __init__(self, db):
        self.db = db

    def add(self):

        Logger.log("Add Item Opened")

        menu = self.db.get_menu()

        category = input("Enter Category: ").upper()

        if category == "":
            print("Category required")
            Logger.log("Add Item Failed - Empty Category")
            return

        item_id = input("Enter Item ID: ")

        if not item_id.isdigit():
            print("Item ID must be number")
            Logger.log("Add Item Failed - Invalid Item ID")
            return

        item_id = int(item_id)

        name = input("Enter Item Name: ")

        if name == "":
            print("Item name required")
            Logger.log("Add Item Failed - Empty Name")
            return

        # check duplicate ID
        for items in menu.values():
            for item in items:
                if item["id"] == item_id:
                    print("Item ID already exists")
                    Logger.log(f"Add Item Failed - Duplicate ID {item_id}")
                    return

        item_type = input("Type (single/double): ").lower()

        # Double item
        if item_type == "double":

            half = input("Enter Half Price: ")
            full = input("Enter Full Price: ")

            if not half.isdigit() or not full.isdigit():
                print("Price must be number")
                Logger.log("Add Item Failed - Invalid Price")
                return

            item = {
                "id": item_id,
                "name": name,
                "type": "double",
                "half": int(half),
                "full": int(full)
            }

        # Single item
        else:

            price = input("Enter Price: ")

            if not price.isdigit():
                print("Price must be number")
                Logger.log("Add Item Failed - Invalid Price")
                return

            item = {
                "id": item_id,
                "name": name,
                "type": "single",
                "price": int(price)
            }

        # create category if not exist
        if category not in menu:
            menu[category] = []

        menu[category].append(item)

        self.db.write_menu(menu)

        print("Item Added Successfully")

        Logger.log(f"Item Added - {name} ID {item_id} Category {category}")