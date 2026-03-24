class ViewMenu:

    def __init__(self, db):
        self.db = db

    def show(self):
        menu = self.db.get_menu()

        if not menu:
            print("No Menu Available ❌")
            return
        
        print("\n=================== 🍽 MENU 🍽 ====================")

        for category, items in menu.items():
            print(f"\n📌 {category}")

            print(f"{'ID':<5} {'NAME':<25} {'HALF ₹':<10} {'FULL ₹':<10}")
            print("-" * 55)

            for item in items:
                 print(f"{item['id']:<5} {item['name']:<25} ₹{item['half']:<9} ₹{item['full']:<9}")


