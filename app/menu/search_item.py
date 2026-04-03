from app.logs.logger import Logger


class SearchItem:

    def __init__(self, db):
        self.db = db

    def search(self):

        menu = self.db.get_menu()

        if not menu:
            print("Menu not available")
            Logger.log("Search Failed - Menu Empty")
            return

        print("\n===== SEARCH MENU =====")

        category = input("Enter Category Name: ").lower()

        found = False

        for cat, items in menu.items():

            if cat.lower() == category:

                print("\n" + "="*65)
                print(f"🍽️ ============= {cat.upper()} ============= 🍽️")
                print("="*65)

                print(f"{'ID':<5} {'Item':<25} {'Type':<8} {'Half':<10} {'Full':<10}")
                print("-"*65)

                for item in items:

                    if item["type"] == "double":

                        print(
                            f"{item['id']:<5} "
                            f"{item['name']:<25} "
                            f"{'Double':<8} "
                            f"₹{item['half']:<10} "
                            f"₹{item['full']:<10}"
                        )

                    else:

                        print(
                            f"{item['id']:<5} "
                            f"{item['name']:<25} "
                            f"{'Single':<8} "
                            f"{'-':<10} "
                            f"₹{item['price']:<10}"
                        )

                found = True
                Logger.log(f"Category Search - {category}")

        if not found:
            print("Category Not Found")
            Logger.log(f"Search Failed - {category}")