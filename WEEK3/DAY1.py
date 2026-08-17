# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# class Ship(Vehicle):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# veh1 = Vehicle("BMW", "M8", 2022)
# ship1 = Ship("Yacht", "Yacht", 2026)

# for x in (veh1, ship1):
#      print(x.brand, x.model, x.year)

class BankAccount:
    def __init__(self, account_title, account_num, balance):
        self.account_title = account_title
        self.__account_num =  account_num
        self.__balance = balance

    def showBankAccountDetail(self):
        print(f"Account Title: {self.account_title}")
        print(f"Account Num: {self.__account_num}")
        print(f"Account Balance: {self.__balance}") 

    def deposit(self, amount):
        self.__balance += amount
        self.showBankAccountDetail()

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            self.showBankAccountDetail()
        else:
            print("Invalid deposit Amount.")

account = BankAccount("Nouman", 200, 1000)
account.deposit(500)
account.withdraw(5000)
