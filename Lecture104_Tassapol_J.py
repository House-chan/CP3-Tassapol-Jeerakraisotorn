class Test:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("add",self.name,self.lastname)

while True:
    x = Test()
    x.name = input("Name:")
    x.lastname = input("Lastname:")
    x.addCart()
