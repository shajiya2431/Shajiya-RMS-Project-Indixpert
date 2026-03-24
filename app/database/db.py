import json

USER_FILE = "app/database/user.json"
MENU_FILE = "app/database/menu.json"

class Database:

    def read_data(self):
        try:
            with open(USER_FILE, "r") as file:
                return json.load(file)
        except:
            return []
        
    def write_users(self, data):
        with open(USER_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def add_user(self, user):
        data = self.read_data()
        data.append(user)
        self.write_users(data)

    def get_all_users(self):
        return self.read_data()
    
    def read_menu(self):
        try:
            with open(MENU_FILE, "r") as file:
                return json.load(file)
        except:
            return {"menu": {}}
    
    def write_menu(self, data):
        with open(MENU_FILE, "w") as file:
            json.dump(data, file, indent = 4)

    def get_menu(self):
        data = self.read_menu()
        return data.get("menu", {})
    
    



    



   