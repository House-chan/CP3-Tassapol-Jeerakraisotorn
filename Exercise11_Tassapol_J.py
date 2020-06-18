x = int(input("???"))
for i in range(x):
    x -= 1
    serie = 1 + i * 2
    print(" " * x,"*" * serie," " * x)
