def login():
    name = "house3d"
    password = "30052545"
    while True:
        ty1 = input("username:")
        ty2 = input("password:")
        if name == ty1:
            if password == ty2:
                print("login Complete")
                break
            else:
                print("login failed")
        else:
            print("username or password unknown")

def Menu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def MenuSelect():
    userSelected = int(input("Select:"))
    return userSelected

def VatCalculator():
    if MenuSelect() == 1:
        price = int(input("price:"))
        print(Price * 1.07)

def PriceCalculator():
    if MenuSelect() == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1 + price2)

login()
Menu()
MenuSelect()
VatCalculator()
PriceCalculator()