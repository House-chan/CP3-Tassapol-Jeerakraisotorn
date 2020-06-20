#Use list
menulist = []
pricelist = []
total = 0
while True:
    menuname = input("enter menu name:").capitalize()
    if menuname == "Exit":
        break
    else:
        price = int(input("Price:"))
        menulist.append(menuname)
        pricelist.append(price)
        total += price
for x in range(len(menulist)):
    print(menulist[x],":",pricelist[x])

print(total)


#Use dictionary
total = 0
menu = {}
while True:
    menuname = input("enter menu name:").capitalize()
    if menuname == "Exit":
        break
    else:
        price = int(input("Price:"))
        menu[menuname] = price
        total += price
for x in menu.keys():
print(x,":",menu[x])
print(total)
