def login():
    username = "house-chan"
    password = '30052545'
    while True:
        userinput = input("enter username:")
        passinput = input("enter password:")
        if userinput == username:
            if password == passinput:
                print("Login Complete")
                return userinput.capitalize()
                break
            else:
                print("Password wrong")
        else:
            print("login failed")
        print("please try again")
login()
Menu = {
    "Fish":50,
    "Chicken":40,
    "Pork":35
}
totallist = []
selectmenu = []
total = 0
while True:
    print("menu")
    print("fish : 50 THB")
    print("chicken : 40 THB")
    print("pork : 35 THB")
    select = input("enter menu:").capitalize()
    if select == "Exit":
        break
    qulity = int(input("Enter Qulity:"))
    selectmenu.append([select,qulity])
    totallist.append(qulity * Menu.get(select))
for x in range(len(totallist)):
    print(selectmenu[x][0],"x",selectmenu[x][1],":",totallist[x])
    total += totallist[x]
print("Total :",total)