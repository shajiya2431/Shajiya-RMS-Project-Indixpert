import uuid 
import getpass
from app.logs.logger import Logger

class Signup:
    def __init__(self, db):
        self.db = db

    def signup_user(self):
        print("\n===== SIGNUP =====")

        Logger.log("Signup Opened")

        user_id = str(uuid.uuid4())
        print("User ID:", user_id)

        username = input("Enter Username: ")
        if username == "" or not username.isalnum():
            print("Invalid Username")
            Logger.log("Signup Failed - Invalid Username")
            return None 
        
        email = input("Enter Email: ")
        if "@" not in email or "." not in email:
            print("Invalid Email")
            Logger.log("Signup Failed - Invalid Email")
            return None 
        
        users = self.db.get_all_users()
        for user in users:
            if user["email"] == email:
                print("Email already exists")
                Logger.log(f"Signup Failed - Email Exists {email}")
                return None 
            
        password = getpass.getpass("Enter Password: ")
        if len(password) < 6:
            print("Invalid password")
            Logger.log("Signup Failed - Weak Password")
            return None 
        
        role = "staff"

        Logger.log(f"Signup Success - {username} ({email})")

        return {
            "id": user_id,
            "username": username,
            "email": email,
            "password": password,
            "role": role
        }



        