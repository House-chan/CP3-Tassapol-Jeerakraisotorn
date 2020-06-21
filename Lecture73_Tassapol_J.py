menuall = []
menulist = {"A":50,"B":45,"C":35}
total = 0
while True:
    menuname = input("enter menu name:").capitalize()
    if menuname == "Exit":
        break
    elif menuname not in menulist:
        print("non of this menu")
        pass
    else:
        total += menulist.get(menuname)
        menuall.append([menuname,menulist[menuname]])
for x in range(len(menuall)):
    print(menuall[x][0],":",menuall[x][1])
print("total:",total)