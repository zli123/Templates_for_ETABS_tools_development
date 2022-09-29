from tkinter import *
from tkinter.ttk import *

colors = ["#FFFFFF", "#00FF65", "#FF9E35", "#0097BD", "#FFFF65", "#D58CBC", "#BBE1DA", "#EABFEF", "#A82F57", "#9CDF27"]

root = Tk()
buttonDict = {}
for i in range(len(colors)):
    #buttonDict[i] = Button(root, text = str(i), bg = colors[i], width = 20)
    buttonDict[i] = Label(root, text = str(i), foreground = colors[i], font = "bold")
    buttonDict[i].pack()

root.mainloop()