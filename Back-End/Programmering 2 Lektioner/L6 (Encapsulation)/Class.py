class Bank:
    def __init__(self, Account, Balance):
        self.__Account = Account
        self.__Balance = Balance
    def CheckBalance(self):
        print(f"You have {self.__Balance} in account {self.__Account}")
    def Deposit(self):
        Cash = float(input("How much would you like to add?"))
        self.__Balance = self.__Balance + Cash
        print(f"{Cash} added, you now have {self.__Balance} in account {self.__Account}")
    def Withdraw(self):
        try:
            Cash = float(input("How much would you like to withdraw?"))
            if self.__Balance > Cash:
                self.__Balance = self.__Balance - Cash
                print(f"Withdrawal successful, you have {self.__Balance} left in your account")
            else: 
                print("Not enough balance in account")
        except ValueError:
            print("Bad input, only put in whole numbers")