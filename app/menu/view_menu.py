from app.logs.logger import Logger


class ViewMenu:

    def __init__(self, db):
        self.db = db

    def show(self):

        Logger.log("View Menu Opened")

        menu = self.db.get_menu()

        if not menu:
            print("Menu not available")
            Logger.log("View Menu Failed - Menu Not Available")
            return

        print("\n" + "="*65)
        print("🍽️ ==============  RESTAURANT MENU  =============  🍽️")
        print("="*65)

        for category, items in menu.items():

            print(f"\n {category}")
            print("-"*65)
            print(f"{'ID':<5} {'ITEM NAME':<25} {'HALF':<10} {'FULL':<10}")
            print("-"*65)

            for item in items:

                # Double Item
                if item.get("type") == "double":
                    print(
                        f"{item.get('id', '-'):<5} "
                        f"{item.get('name', '-'):<25} "
                        f"₹{item.get('half', '-'):<10} "
                        f"₹{item.get('full', '-'):<10}"
                    )

                # Single Item
                else:
                    print(
                        f"{item.get('id', '-'):<5} "
                        f"{item.get('name', '-'):<25} "
                        f"{'-':<10} "
                        f"₹{item.get('price', '-'):<10}"
                    )

        print("\n" + "="*65)

        Logger.log("Menu Viewed Successfully")