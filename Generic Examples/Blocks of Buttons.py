import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.logo = tk.Label(self, text="Logo", background="orange")
        self.buttons = []
        for i in range(6):
            self.buttons.append(tk.Button(self, text="Button %s" % (i+1,), background="green"))
        self.other1 = tk.Label(self, background="purple")
        self.other2 = tk.Label(self, background="yellow")
        self.other3 = tk.Label(self, background="pink")
        self.other4 = tk.Label(self, background="gray")
        self.main = tk.Frame(self, background="blue")

        self.logo.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.other1.grid(row=0, column=1, sticky="nsew")
        self.other2.grid(row=0, column=2, sticky="nsew")
        self.other3.grid(row=1, column=1, sticky="nsew")
        self.other4.grid(row=1, column=2, sticky="nsew")
        self.buttons[0].grid(row=2, column=0, sticky="nsew")
        self.buttons[1].grid(row=3, column=0, sticky="nsew")
        self.buttons[2].grid(row=4, column=0, sticky="nsew")
        self.buttons[3].grid(row=5, column=0, sticky="nsew")
        self.buttons[4].grid(row=6, column=0, sticky="nsew")
        self.buttons[5].grid(row=7, column=0, sticky="nsew")
        self.main.grid(row=2, column=2, columnspan=2, rowspan=6)

        for row in range(8):
            self.grid_rowconfigure(row, weight=1)
        for col in range(3):
            self.grid_columnconfigure(col, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.geometry("800x400")
    root.mainloop()