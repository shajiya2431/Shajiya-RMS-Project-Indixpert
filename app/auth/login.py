import getpass

class Login:

    def __init__(self, db):
        self.db = db
    
    def check_login(self):
        print("\n===== LOGIN =====")

        user_input = input("Enter Username or Email: ")
        password = getpass.getpass("Enter password: ")

        users = self.db.get_all_users()

        for user in users:
            if (user["username"] == user_input or user["email"] == user_input) and user["password"] == password:
                return user
            
        return None
    





       