from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox


# Taken from: https://stackoverflow.com/a/17985217/11106801
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle


class Radiobutton:
    def __init__(self, canvas, text="", variable=None, value=0, radius=10,
                 fill="black"):
        self.canvas = canvas
        self.variable = variable
        self.fill = fill
        self.text = text
        self.value = value
        self.radius = radius

        self.variable.trace("w", self.redraw)

        self.circle = None

    def put(self, x, y):
        self.x = x
        self.y = y
        self.canvas.create_circle(x, y, self.radius, outline=self.fill)
        self.canvas.create_text(x + 2*self.radius, y, text=self.text,
                                fill=self.fill, anchor="w")
        self.redraw()
        self.canvas.bind("<Button-1>", self.select, add=True)

    def select(self, event):
        if (self.x - event.x)**2 + (self.y - event.y)**2 <= self.radius**2:
            self.variable.set(self.value)
            self.redraw()

    def create_circle(self):
        self.circle = self.canvas.create_circle(self.x, self.y, self.radius-4,
                                                outline=self.fill,
                                                fill=self.fill)

    def redraw(self, *args):
        if self.value == self.variable.get():
            if self.circle is None:
                self.create_circle()
        else:
            if self.circle is not None:
                self.canvas.delete(self.circle)
                self.circle = None


class GUI_Prog:
    def __init__(self):
            root = Tk()
            root.title("Risk Analysis")
            root.geometry("1100x630")
            r = IntVar()

            #Setting up Canvas:
            my_canvas = Canvas(root, width=1100, height=630)
            my_canvas.pack(fill="both", expand=True)

            #Background:

            bg = PhotoImage(file="C:\\Users\\neeraj\\Desktop\\Class\\Python\\programs\\resources\\images\\background4cut.png")
            my_canvas.create_image(0, 0, image=bg, anchor="nw")

            #Creating title text:
            my_canvas.create_text(540, 40, text="Risk Analysis",
                                  font=("Times", 30), fill="white")
            my_canvas.create_text(140, 100, text="1) Do you smoke?",
                                  font=("helvetica", 15), fill="black")

            but_1 = Radiobutton(my_canvas, text="yes", variable=r, value=1,
                                fill="white")
            but_1.put(60, 150)

            but_2 = Radiobutton(my_canvas, text="no", variable=r, value=2,
                                fill="white")
            but_2.put(150, 150)

            r.set(1)

            root.mainloop()


obj = GUI_Prog()