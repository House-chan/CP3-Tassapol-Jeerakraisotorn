import tkinter
def Calculate(event):
    x = float(entryW.get())/((float(entryH.get())/100)**2)
    print(x)
    labelR.configure(text = x,font = 35)
    if x >= 30:
        labelR2.configure(text = "Fat",fg = "Red",bg = "White")
    elif x >= 25:
        labelR2.configure(text="Plump",fg = "Yellow",bg = "White")
    elif x >= 20:
        labelR2.configure(text="Average",bg = "White")
    else:
        labelR2.configure(text="Skinny",fg = "Red",bg = "White")


window = tkinter.Tk()

labelH = tkinter.Label(window,text = "Height (cm.)").grid(row = 0, column = 0)
entryH = tkinter.Entry(window)
entryH.grid(row = 0,column = 1)
labelW = tkinter.Label(window,text = "Weight (Kg.)").grid(row = 1,column = 0)
entryW = tkinter.Entry(window)
entryW.grid(row = 1,column = 1)
button = tkinter.Button(window,text = "Calculate")
button.bind("<Button-1>",Calculate)
button.grid(row = 2,column = 0)
labelR = tkinter.Label(window,text = "")
labelR.grid(row = 4,column = 0)
labelR2 = tkinter.Label(window,text = "")
labelR2.grid(row = 5,column = 0)
window.mainloop()
