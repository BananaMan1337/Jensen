
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
    balanceadd = float(input("How much balance would you like to add?"))
    confirmation = input("Are you sure you want to add this amount? Y/N").lower
    accepted_strings={"yes","y","ja"}
    if confirmation in accepted_strings:
        wallet = wallet + balanceadd
        print ("Balance added!")
        break
    else: continue

while True:
    ShoppingPath = input("What would you like to buy?\n Milk\t Bread\t Candy\t Check Wallet").lower
    if ShoppingPath == "milk":
        input("Milk is $2, would you like to purchase?")
        if input in accepted_strings:
            result=purchase(wallet,2)
            successful = result[0]
            wallet = result[1]
            if successful == True:
                print("Milk purchased! It will arrive in 2-3 business days.")
                
            else: continue
    elif ShoppingPath =="bread":
        input("Bread is $5, would you like to purchase?")
        if input in accepted_strings:
            result=purchase(wallet,5)
            successful = result[0]
            wallet = result[1]
            if successful == True:
                print("Bread purchased! It will arrive in 2-3 business days.")
                
            else: continue
    elif ShoppingPath =="candy":
        input("candy is $1, would you like to purchase?")
        if input in accepted_strings:
            result=purchase(wallet,1)
            successful = result[0]
            wallet = result[1]
            if successful == True:
                print("Milk purchased! It will arrive in 2-3 business days.")
                
            else: continue
    elif ShoppingPath=="wallet":
        print(wallet)
    else: continue


