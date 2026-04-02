from app.logs.logger import Logger
from app.logs.logger import Logger
import getpass

class Login:

    def __init__(self, db):
        self.db = db

    def check_login(self):
        print("\n====== LOGIN ======")

        user_input = input("Enter Username or Email: ")

        if user_input == "":
            print("Username/Email required")
            Logger.log("Login Faild - Empty Username")
            return None
        
        password = getpass.getpass("Enter password: ")

        if password == "":
            Logger.log("Login Faild - Empty Password")
            return None 
        
        users = self.db.get_all_users()

        for user in users:
            if (user["username"] == user_input or user["email"] == user_input) and user["password"] == password:

                Logger.log(f"Login Success - {user['username']} ({user['role']})")

                return user
            
        Logger.log(f"Login Failed - {user_input}")

        print("Invalid Username or Password")

        return None 


