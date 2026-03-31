from app.auth.signup import Signup
from app.auth.login import Login
from app.database.db import Database
from app.dashboard.admin_dashboard import AdminDashboard
from app.dashboard.staff_dashboard import StaffDashboard
from app.logs.logger import Logger



class UserManager:

    def __init__(self):
        self.db = Database()
        self.signup = Signup(self.db)
        self.login = Login(self.db)

    def start(self):

        Logger.log("System Started")

        while True:
            print("\n~~~~~~~~~~~~~~~~~~~~~ RESTAURANT MANGMENT SYSTEM ~~~~~~~~~~~~~~~~~~~~~~\n")
            print("----- WELCOME -----")
            print("1. Signup")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter a choice: ")

            if choice == "1":

                Logger.log("Signup Selected")

                user = self.signup.signup_user()

                if user:
                    self.db.add_user(user)
                    print("Signup Successful")

                    Logger.log(f"Signup Success - {user['username']}")

            elif choice == "2":

                Logger.log("Login Selected")

                user = self.login.check_login()

                if user:
                    print("Login Successful")

                    Logger.log(f"Login Success - {user['username']}")

                    if user.get("role") == "admin":

                        Logger.log("Admin Dashboard Opened")
                        AdminDashboard().menu()

                    else:

                        Logger.log("Staff Dashboard Opened")
                        StaffDashboard().menu()

                else:
                    print("Invalid Credentials")
                    Logger.log("Login Failed")

            elif choice == "3":
                print("Exit")
                Logger.log("System Exit")
                break

            else:
                print("Invalid choice")
                Logger.log("Invalid Choice Entered")





              