import uuid
import getpass
from app.logs.logger import Logger


class Signup:
    def __init__(self, db):
        self.db = db

    def signup_user(self):
        print("\n===== SIGNUP =====")

        Logger.log("Signup Opened")

        # Generate User ID
        user_id = str(uuid.uuid4())
        print("User ID:", user_id)

        # Username
        username = input("Enter Username: ")

        # Username Validation
        if username == "" or not username.isalnum() or username.isdigit():
            print("Invalid Username")
            Logger.log("Signup Failed - Invalid Username")
            return None

        # Email
        email = input("Enter Email: ")

        # Email Validation
        if "@" not in email or "." not in email:
            print("Invalid Email")
            Logger.log("Signup Failed - Invalid Email")
            return None

        # Check Duplicate Email
        users = self.db.get_all_users()
        for user in users:
            if user["email"] == email:
                print("Email already exists")
                Logger.log(f"Signup Failed - Email Exists {email}")
                return None

        # Password
        password = getpass.getpass("Enter Password: ")

        # Password Validation
        if len(password) < 6:
            print("Password must be at least 6 characters")
            Logger.log("Signup Failed - Weak Password")
            return None

        # Role
        role = "staff"

        Logger.log(f"Signup Success - {username} ({email})")

        # Return User Data
        return {
            "id": user_id,
            "username": username,
            "email": email,
            "password": password,
            "role": role
        }