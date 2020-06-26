import tkinter
def Calculator(event):
    x = float(entryW.get())/((float(entryH.get()))/100)**2
    print(x)
    result.configure(text = x)
    if x >= 30:
        result2.configure(text = "Very Fat",fg = "Red")
    elif x >= 25:
        result2.configure(text="Fat", fg="Red")
    elif x >= 23:
        result2.configure(text = "Plump",fg = "Yellow")
    elif x >= 18.6:
        result2.configure(text = "Average")
    else:
        result2.configure(text = "Skinny",fg = "Red")


window = tkinter.Tk()
head = tkinter.Label(text = "BMI Calculator",font = 50).grid(row = 0, column = 1)
height = tkinter.Label(text = "Height (cm.)").grid(row = 1, column = 0)
entryH = tkinter.Entry()
entryH.grid(row = 1, column = 1)
weight = tkinter.Label(text = "Weight (Kg.)").grid(row = 2, column = 0)
entryW = tkinter.Entry()
entryW.grid(row = 2,column = 1)
button = tkinter.Button(text = "Calculate",font = 40)
button.bind("<Button-1>",Calculator)
button.grid(row = 3)
result = tkinter.Label(text = "",font = 40,bg = "White")
result.grid(row = 4, column = 0)
result2 = tkinter.Label(text = "",font = 45,bg = "white")
result2.grid(row = 4, column = 1)
window.mainloop()
