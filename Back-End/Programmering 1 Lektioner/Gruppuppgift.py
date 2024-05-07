
def purchase (wallet, price):
    if wallet >= price:
        wallet = wallet - price
        print("Purchase successful! You have",wallet,"balance left")
        return True, wallet
    else:
        print("Not enough balance")
        return False, wallet
wallet = 0
while True:
    try:
        balanceadd = float(input("How much balance would you like to add?"))
        confirm = input("Are you sure you want to add this amount? Y/N").lower()
        accepted_strings=("yes","y","ja")
        if confirm in accepted_strings:
            wallet = wallet + balanceadd
            print ("Balance added!")
            break
    except ValueError:
        print("Please enter only numbers.")
        continue

while True:
    ShoppingPath = input("What would you like to browse?\n Milk\t Bread\t Candy\t Wallet").lower()
    if ShoppingPath == "milk":
        milkchoice = input("Milk is $2, would you like to purchase?").lower()
        if milkchoice in accepted_strings:
            result=purchase(wallet,2)
            successful = result[0]
            wallet = result[1]
            if successful == True:
                print("Milk purchased! It will arrive in 2-3 business days.")
                continue
            else: continue
    elif ShoppingPath =="bread":
        breadchoice=input("Bread is $5, would you like to purchase?").lower()
        if breadchoice in accepted_strings:
            result=purchase(wallet,5)
            successful = result[0]
            wallet = result[1]
            if successful == True:
                print("Bread purchased! It will arrive in 2-3 business days.")
                continue
            else: continue
    elif ShoppingPath =="candy":
        candychoice=input("candy is $1, would you like to purchase?").lower()
        if candychoice in accepted_strings:
            result=purchase(wallet,1)
            successful = result[0]
            wallet = result[1]
            if successful == True:
                print("Candy purchased! It will arrive in 2-3 business days.")
                continue
            else: continue
    elif ShoppingPath=="wallet":
        print("You have $",wallet,"in your balance.")
        continue
    else: continue


