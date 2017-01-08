# Bailey Thompson
# Graphing Calculator (Alpha 1.0.0)
# 8 January 2017
# Info: This programs is intended to graph functions.
# TODO: make buttons work (the only current working button is Enter)
from tkinter import *
from tkinter import ttk

size = 10
formula = "x"


def translate(x, y):
    tc = [0, 0]
    x_mul = int(canvas["width"]) / (size * 2)
    y_mul = (int(canvas["height"]) / (size * -2))
    x = (x + size) * x_mul
    y = (y + size) * y_mul + int(canvas["height"])
    tc[0] = x
    tc[1] = y
    return tc


def draw_line(xfrom, yfrom, xto, yto, colour):
    fromcoords = translate(xfrom, yfrom)
    tocoords = translate(xto, yto)
    canvas.create_line(fromcoords[0], fromcoords[1], tocoords[0], tocoords[1], fill=colour)


def draw_grid():
    draw_line(size * -1, 0, size, 0, "black")
    draw_line(0, size * -1, 0, size, "black")


def draw_graph(event):
    canvas.delete("all")
    draw_grid()
    yprev = 0.0
    x = size * -1
    while x <= size:
        y = eval(formula)
        draw_line(x - 0.25, yprev, x, y, "black")
        yprev = y
        x += 0.25


root = Tk()

root.wm_title("Graphing Calculator")
root.resizable(width=False, height=False)

horizontalScreen = root.winfo_screenwidth() / 2 - root.winfo_reqwidth()
verticalScreen = root.winfo_screenheight() / 2 - root.winfo_reqheight()
root.geometry("+%d+%d" % (horizontalScreen, verticalScreen))

canvas = Canvas(root)
functionDisplay = Label(root, text="f(x) = x").grid(row=1, column=0)

btn0 = ttk.Button(root, text="0").grid(row=2, column=0)
btn1 = ttk.Button(root, text="1").grid(row=2, column=1)
btn2 = ttk.Button(root, text="2").grid(row=2, column=2)
btn3 = ttk.Button(root, text="3").grid(row=2, column=3)
btn4 = ttk.Button(root, text="4").grid(row=2, column=4)

btn5 = ttk.Button(root, text="5").grid(row=3, column=0)
btn6 = ttk.Button(root, text="6").grid(row=3, column=1)
btn7 = ttk.Button(root, text="7").grid(row=3, column=2)
btn8 = ttk.Button(root, text="8").grid(row=3, column=3)
btn9 = ttk.Button(root, text="9").grid(row=3, column=4)

btnSin = ttk.Button(root, text="sin").grid(row=4, column=0)
btnCos = ttk.Button(root, text="cos").grid(row=4, column=1)
btnTan = ttk.Button(root, text="tan").grid(row=4, column=2)
btnLog = ttk.Button(root, text="log").grid(row=4, column=3)
btnLn = ttk.Button(root, text="ln").grid(row=4, column=4)

btnCsc = ttk.Button(root, text="arcsin").grid(row=5, column=0)
btnSec = ttk.Button(root, text="arccos").grid(row=5, column=1)
btnCot = ttk.Button(root, text="arctan").grid(row=5, column=2)
btnPi = ttk.Button(root, text="π").grid(row=5, column=3)
btnE = ttk.Button(root, text="e").grid(row=5, column=4)

btnPlus = ttk.Button(root, text="+").grid(row=6, column=0)
btnMinus = ttk.Button(root, text="-").grid(row=6, column=1)
btnMultiply = ttk.Button(root, text="*").grid(row=6, column=2)
btnDivide = ttk.Button(root, text="/").grid(row=6, column=3)
btnExponent = ttk.Button(root, text="^").grid(row=6, column=4)

btnLeftBracket = ttk.Button(root, text="(").grid(row=7, column=0)
btnRightBracket = ttk.Button(root, text=")").grid(row=7, column=1)
btnDelete = ttk.Button(root, text="Delete").grid(row=7, column=2)
btnClear = ttk.Button(root, text="Clear").grid(row=7, column=3)
btnEnter = ttk.Button(root, text="Enter")

btnX = ttk.Button(root, text="x").grid(row=8, column=0)
btnZoomIn = ttk.Button(root, text="Zoom In").grid(row=8, column=1)
btnZoomOut = ttk.Button(root, text="Zoom Out").grid(row=8, column=2)
btnExit = ttk.Button(root, text="Exit Application").grid(row=8, column=3, columnspan=2, sticky=W+E)

btnEnter.bind('<Button-1>', draw_graph)

btnEnter.grid(row=7, column=4)
canvas.grid(row=0, column=0, columnspan=5)

draw_grid()

root.mainloop()