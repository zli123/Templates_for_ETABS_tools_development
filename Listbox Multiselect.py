from tkinter import *
from tkinter.ttk import *

storyDict = {"05": 5, "04": 4, "03": 3, "02": 2, "01": 1, "fgggf": 50, "sdfgfg" : 0}
usedPierLabels = ["abc", "def", "ghi", "rtf", "ertge", "rrs"]
activeStories = []
activePiers = []

availableStories = []
for i in storyDict:
    if i not in activeStories:
        availableStories.append(i)

availablePiers = []
for i in usedPierLabels:
    if i not in activePiers:
        availablePiers.append(i)

root = Tk()
root.title("Active Parameters")
root.geometry("400x500")
root.resizable(0, 0)

def getValue(elem):
    return storyDict[elem]

def addPiers():
    temp = [optionAvailablePiers.get(i) for i in optionAvailablePiers.curselection()]
    temp.sort(reverse=True)
    temp2 = optionActivePiers.get(0, END)
    result = [i for i in temp2]
    for i in range(len(temp)):
        optionAvailablePiers.delete(availablePiers.index(temp[i]))
        availablePiers.pop(availablePiers.index(temp[i]))
        result.append(temp[i])
    result.sort()
    activePiers.clear()
    optionActivePiers.delete(0, END)
    for i in range(len(result)):
        optionActivePiers.insert(END, result[i])
        activePiers.append(result[i])

def addAllPiers():
    for i in availablePiers:
        activePiers.append(i)
        optionActivePiers.insert(END, i)
    optionAvailablePiers.delete(0, END)
    availablePiers.clear()

def deletePiers():
    temp = [optionActivePiers.get(i) for i in optionActivePiers.curselection()]
    temp.sort(reverse=True)
    temp2 = optionAvailablePiers.get(0, END)
    result = [i for i in temp2]
    for i in range(len(temp)):
        optionActivePiers.delete(activePiers.index(temp[i]))
        activePiers.pop(activePiers.index(temp[i]))
        result.append(temp[i])
    result.sort()
    availablePiers.clear()
    optionAvailablePiers.delete(0, END)
    for i in range(len(result)):
        optionAvailablePiers.insert(END, result[i])
        availablePiers.append(result[i])

def deleteAllPiers():
    for i in activePiers:
        availablePiers.append(i)
        optionAvailablePiers.insert(END, i)
    optionActivePiers.delete(0, END)
    activePiers.clear()

def addStories():
    temp = [optionAvailableStories.get(i) for i in optionAvailableStories.curselection()]
    temp.sort(reverse=True)
    temp2 = optionActiveStories.get(0, END)
    result = [i for i in temp2]
    for i in range(len(temp)):
        optionAvailableStories.delete(availableStories.index(temp[i]))
        availableStories.pop(availableStories.index(temp[i]))
        result.append(temp[i])
    result.sort(reverse=True, key=getValue)
    activeStories.clear()
    optionActiveStories.delete(0, END)
    for i in range(len(result)):
        optionActiveStories.insert(END, result[i])
        activeStories.append(result[i])

def addAllStories():
    for i in availableStories:
        activeStories.append(i)
        optionActiveStories.insert(END, i)
    activeStories.sort(reverse=True, key=getValue)
    optionAvailableStories.delete(0, END)
    availableStories.clear()

def deleteStories():
    temp = [optionActiveStories.get(i) for i in optionActiveStories.curselection()]
    temp.sort(reverse=True)
    temp2 = optionAvailableStories.get(0, END)
    result = [i for i in temp2]
    for i in range(len(temp)):
        optionActiveStories.delete(activeStories.index(temp[i]))
        activeStories.pop(activeStories.index(temp[i]))
        result.append(temp[i])
    result.sort(reverse=True, key=getValue)
    availableStories.clear()
    optionAvailableStories.delete(0, END)
    for i in range(len(result)):
        optionAvailableStories.insert(END, result[i])
        availableStories.append(result[i])

def deleteAllStories():
    for i in activeStories:
        availableStories.append(i)
        optionAvailableStories.insert(END, i)
    availableStories.sort(reverse=True, key=getValue)
    optionActiveStories.delete(0, END)
    activeStories.clear()


#Labels
instructionActivePiers = Label(root, text = "Active Pier Labels")
instructionActivePiers.place(relx = 0.38, rely = 0.05, anchor = W)


instructionActiveStories = Label(root, text = "Active Story Levels")
instructionActiveStories.place(relx = 0.38, rely = 0.52, anchor = W)

#Buttons
optionInsertPiers = Button(root, width = 5, text = ">", command = addPiers)
optionInsertPiers.place(relx = 0.44, rely = 0.18, anchor = W)

optionInsertAllPiers = Button(root, width = 5, text = ">>", command = addAllPiers)
optionInsertAllPiers.place(relx = 0.44, rely = 0.23, anchor = W)

optionRemovePiers = Button(root, width = 5, text = "<", command = deletePiers)
optionRemovePiers.place(relx = 0.44, rely = 0.33, anchor = W)

optionRemoveAllPiers = Button(root, width = 5, text = "<<", command = deleteAllPiers)
optionRemoveAllPiers.place(relx = 0.44, rely = 0.38, anchor = W)

optionInsertStories = Button(root, width = 5, text = ">", command = addStories)
optionInsertStories.place(relx = 0.44, rely = 0.63, anchor = W)

optionInsertAllStories = Button(root, width = 5, text = ">>", command = addAllStories)
optionInsertAllStories.place(relx = 0.44, rely = 0.68, anchor = W)

optionRemoveStories = Button(root, width = 5, text = "<", command = deleteStories)
optionRemoveStories.place(relx = 0.44, rely = 0.78, anchor = W)

optionRemoveAllStories = Button(root, width = 5, text = "<<", command = deleteAllStories)
optionRemoveAllStories.place(relx = 0.44, rely = 0.83, anchor = W)


#Listboxes

#frm = Frame(activeItems, height = 280)
frm = Frame(root, height = 280)
frm.place(relx = 0.05, rely = 0.28, anchor = W)

optionAvailablePiers = Listbox(frm, height = 12, width = 20, selectmode = "multiple")
for i in availablePiers:
    optionAvailablePiers.insert(END, i)
optionAvailablePiers.pack(side = "left", fill = "y")


#frm2 = Frame(activeItems, height = 280)
frm2 = Frame(root, height = 280)
frm2.place(relx = 0.6, rely = 0.28, anchor = W)

optionActivePiers = Listbox(frm2, height = 12, width = 20, selectmode = "multiple")
for i in activePiers:
    optionActivePiers.insert(END, i)
optionActivePiers.pack(side = "left", fill = "y")

#frm3 = Frame(activeItems, height = 280)
frm3 = Frame(root, height = 280)
frm3.place(relx = 0.05, rely = 0.75, anchor = W)

optionAvailableStories = Listbox(frm3, height = 12, width = 20, selectmode = "multiple")
for i in availableStories:
    optionAvailableStories.insert(END, i)
optionAvailableStories.pack(side = "left", fill = "y")

#frm4 = Frame(activeItems, height = 280)
frm4 = Frame(root, height = 280)
frm4.place(relx = 0.6, rely = 0.75, anchor = W)

optionActiveStories = Listbox(frm4, height = 12, width = 20, selectmode = "multiple")
for i in activeStories:
    optionActiveStories.insert(END, i)
optionActiveStories.pack(side = "left", fill = "y")

#Scrollbars

scrollbar = Scrollbar(frm, orient = "vertical")
scrollbar.pack(side = "right", fill = "y")

scrollbar.config(command = optionAvailablePiers.yview)
optionAvailablePiers.config(yscrollcommand = scrollbar.set)

scrollbar2 = Scrollbar(frm2, orient = "vertical")
scrollbar2.pack(side = "right", fill = "y")

scrollbar2.config(command = optionActivePiers.yview)
optionActivePiers.config(yscrollcommand = scrollbar2.set)

scrollbar3 = Scrollbar(frm3, orient = "vertical")
scrollbar3.pack(side = "right", fill = "y")

scrollbar3.config(command = optionAvailableStories.yview)
optionAvailableStories.config(yscrollcommand = scrollbar3.set)

scrollbar4 = Scrollbar(frm4, orient = "vertical")
scrollbar4.pack(side = "right", fill = "y")

scrollbar4.config(command = optionActiveStories.yview)
optionActiveStories.config(yscrollcommand = scrollbar4.set)

root.mainloop()