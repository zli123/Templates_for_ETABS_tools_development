import tkinter as tk

class Run:
    def __init__(self, master):

        self.master = master

        self.button = tk.Button(master, text="TopLevel", command=self.make_new)
        self.button.pack()

    def make_new(self):
        self.button['state'] = 'disabled'

        new = tk.Toplevel(self.master)

        lbl = tk.Label(new, text='only one topLevel')
        lbl.pack()

        new.protocol("WM_DELETE_WINDOW", lambda : self.button.configure(state='normal') or new.destroy()) # or make a method to change the state


master1 = tk.Tk()
i = Run(master1)
master1.mainloop()