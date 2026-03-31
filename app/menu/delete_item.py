from app.logs.logger import Logger


class DeleteItem:

    def __init__(self, db):
        self.db = db

    def delete(self):

        Logger.log("Delete Item Opened")

        menu = self.db.get_menu()

        item_id = input("Enter Item ID to Delete: ")

        # validation
        if not item_id.isdigit():
            print("Item ID must be number")
            Logger.log("Delete Item Failed - Invalid ID")
            return

        item_id = int(item_id)

        found = False

        for category in list(menu.keys()):
            items = menu[category]

            for item in items:

                if item["id"] == item_id:
                    items.remove(item)
                    found = True
                    print("Item Deleted Successfully")

                    Logger.log(f"Item Deleted - ID {item_id} Category {category}")

            # remove empty category
            if not items:
                del menu[category]

        if not found:
            print("Item not found")
            Logger.log(f"Delete Item Failed - ID {item_id} Not Found")

        self.db.write_menu(menu)