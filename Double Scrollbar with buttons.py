from tkinter import *
from tkinter.ttk import *

class DoubleScrolledFrame:
    """
    A vertically scrolled Frame that can be treated like any other Frame
    ie it needs a master and layout and it can be a master.
    keyword arguments are passed to the underlying Frame
    except the keyword arguments 'width' and 'height', which
    are passed to the underlying Canvas
    note that a widget layed out in this frame will have Canvas as self.master,
    if you subclass this there is no built in way for the children to access it.
    You need to provide the controller separately.
    """
    def __init__(self, master, **kwargs):
        width = kwargs.pop('width', None)
        height = kwargs.pop('height', None)
        self.outer = Frame(master, **kwargs)

        self.vsb = Scrollbar(self.outer, orient = "vertical")
        self.vsb.grid(row = 0, column = 1, sticky='ns')
        self.hsb = Scrollbar(self.outer, orient = "horizontal")
        self.hsb.grid(row = 1, column = 0, sticky = 'ew')
        self.canvas = Canvas(self.outer, highlightthickness = 0, width = width, height = height)
        self.canvas.grid(row = 0, column = 0, sticky = 'nsew')
        self.outer.rowconfigure(0, weight = 1)
        self.outer.columnconfigure(0, weight = 1)
        self.canvas['yscrollcommand'] = self.vsb.set
        self.canvas['xscrollcommand'] = self.hsb.set
        # mouse scroll does not seem to work with just "bind"; You have
        # to use "bind_all". Therefore to use multiple windows you have
        # to bind_all in the current widget
        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)
        self.vsb['command'] = self.canvas.yview
        self.hsb['command'] = self.canvas.xview

        self.inner = Frame(self.canvas)
        # pack the inner Frame into the Canvas with the topleft corner 4 pixels offset
        self.canvas.create_window(4, 4, window = self.inner, anchor = 'nw')
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.outer_attr = set(dir(Widget))

    def __getattr__(self, item):
        if item in self.outer_attr:
            # geometry attributes etc (eg pack, destroy, tkraise) are passed on to self.outer
            return getattr(self.outer, item)
        else:
            # all other attributes (_w, children, etc) are passed to self.inner
            return getattr(self.inner, item)

    def _on_frame_configure(self, event=None):
        x1, y1, x2, y2 = self.canvas.bbox("all")
        height = self.canvas.winfo_height()
        width = self.canvas.winfo_width()
        self.canvas.config(scrollregion = (0 , 0, max(x2, width), max(y2, height)))

    def _bind_mouse(self, event = None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event = None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        func = self.canvas.xview_scroll if event.state & 1 else self.canvas.yview_scroll
        if event.num == 4 or event.delta > 0:
            func(-1, "units" )
        elif event.num == 5 or event.delta < 0:
            func(1, "units" )

    def __str__(self):
        return str(self.outer)

#  **** SCROLL BAR TEST *****
DesignInterface = Tk()
DesignInterface.title("Interactive Design")
DesignInterface.geometry("800x800")

interface = DoubleScrolledFrame(DesignInterface, borderwidth = 2)
interface.pack(side = LEFT, fill = BOTH, expand = True)

labels = Frame(DesignInterface)
labels.pack(expand = True, ipady = 25)

greenLabel = Label(labels, text = "Green: Designed, OK.", foreground = "green")
greenLabel.pack()

redLabel = Label(labels, text = "Red: No section designed.", foreground = "red")
redLabel.pack()

yellowLabel = Label(labels, text = "Yellow: Not yet designed.", foreground = "orange")
yellowLabel.pack()

orangeLabel = Label(labels, text = "Violet: Retained sections.", foreground = "magenta")
orangeLabel.pack()

buttons = Frame(DesignInterface)
buttons.pack(side = BOTTOM, pady = 10)

runAutoDesign = Button(buttons, text = "Run Auto-design", width = 15)#, command = autoDesign)
runAutoDesign.pack(pady = 10, padx = 5, side = LEFT)

OKButton = Button(buttons, text = "OK", width = 10)#, command = refresh)
OKButton.pack(pady = 10, padx = 5, side = RIGHT)

#  **** SCROLL BAR TEST *****
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a = alphabet[1:10]
b = alphabet[2:6]
c = alphabet[9:24]
ae = alphabet[0:10]
ee = alphabet[0:26]
d = [a, b, c, ae, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee, ee]
length = 0
for i in d:
    if(length < len(i)):
        length = len(i)

for i in range(len(d)):
    for j in range(len(d[i])):
        label = Button(interface, text="{}{}".format(d[i][j], i), width = 10)
        label.grid(column=i, row= length-j, sticky='sw', padx=2, pady=2)

DesignInterface.mainloop()