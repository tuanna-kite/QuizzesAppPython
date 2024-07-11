import json


class Account:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_data(self):
        if self.data_path is None:
            raise Exception("data_path is empty!")
        with open(self.data_path, 'r') as fp:
            return json.load(fp)

    def save_data(self, data):
        if self.data_path is None:
            raise Exception("data_path is empty!")
        with open(self.data_path, 'w') as fp:
            return json.dump(data, fp)

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        accounts = self.load_data()
        for account in accounts:
            if account["username"] == username and account["password"] == password:
                print("Login successfully!")
                return account
        print("Login Failed!")
        return None

    def exist(self, username):
        accounts = self.load_data()
        for account in accounts:
            if account["username"] == username:
                return True
        return False

    def register(self, security=None):
        pass


class Admin(Account):
    SECURITY_CODE = '9999'

    def __init__(self):
        super().__init__('admin.json')

    def register(self, security_code=None):
        username = input("Username: ")
        password = input("Password: ")
        if self.exist(username):
            print("Username existed!")
            return

        if security_code != self.SECURITY_CODE:
            print("Wrong security code!")
            return

        accounts = self.load_data()
        account = {
            "username": username,
            "password": password
        }
        accounts.append(account)
        self.save_data(accounts)
        print("Register successfully!")

    def list_users(self):
        user = User()
        accounts = user.load_data()
        print("List User account:")
        print("Username\t\tPassword\t\tFull Name")
        for acc in accounts:
            print(f"{acc['username']}\t\t\t{acc['password']}\t\t\t{acc['fullname']}")


class User(Account):
    def __init__(self):
        super().__init__('user.json')

    def register(self, security_code=None):
        username = input("Username: ")
        password = input("Password: ")
        if self.exist(username):
            print("Username existed!")
            return

        accounts = self.load_data()
        account = {
            "username": username,
            "password": password
        }
        accounts.append(account)
        self.save_data(accounts)
        print("Register successfully!")


if __name__ == '__main__':
    while True:
        print("\n=========== QUIZZES APP ===========")
        print("1. You are Admin")
        print("2. You are User")
        print("3. Exit")
        choice = input("Please input 1 to 3: ")
        if choice == '1':
            admin = Admin()
            admin_info = admin.login()
            if admin_info is not None:
                admin.list_users()
        elif choice == '2':
            user = User()
            user.login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Wrong Choice!")
