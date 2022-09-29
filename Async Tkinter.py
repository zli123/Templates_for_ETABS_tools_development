from tkinter import *
from tkinter.ttk import *
import asyncio


def work():
    async def hitt():
        await asyncio.sleep(1)
        print("Nooooooooooooooooooo")

    async def lol():
        print("Hello")
        await hitt()
        print("World")
    loop = asyncio.new_event_loop()
    loop.run_until_complete(lol())
    print("start")



root = Tk()

but = Button(root, text = "trial", command = work)
but.pack()



root.mainloop()