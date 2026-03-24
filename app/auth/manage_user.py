from app.auth.signup import Signup
from app.auth.login import Login
from app.database.db import Database
from app.dashboard.admin_dashboard import AdminDashboard
from app.dashboard.staff_dashboard import StaffDashboard




class UserManager:

    def __init__(self):
        self.db = Database()
        self.signup = Signup(self.db)
        self.login = Login(self.db)

    def start(self):
        while True:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~ RESTAURANT MANAGMENT SYSTEM ~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("\n===== WELCOME =====")
            print("1. Signup")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter a choice: ")

            if choice == "1":
                user = self.signup.signup_user()

                if user:
                    self.db.add_user(user)
                    print("Signup Successful")

            elif choice == "2":
                user = self.login.check_login()

                if user:
                    print("Login Successful")

                    if user.get("role") == "admin":
                        AdminDashboard().menu()
                        
                    else:
                        StaffDashboard().menu()
                        

                else:
                    print("Invalid Credentials")

            elif choice == "3":
                    print("Exit")

            else:
                print("Invalid choice")
                
            
        
                    

                    

                        


                    