#Use list
menulist = []
total = 0
while True:
    menuname = input("enter menu name:").capitalize()
    if menuname == "Exit":
        break
    else:
        price = int(input("Price:"))
        menulist.append([menuname,price])

        total += price
for x in range(len(menulist)):
    print(menulist[x][0],":",menulist[x][1])
print(total)
