from tkinter import Tk, StringVar
from tkinter import ttk
from tkinter.ttk import Entry

INPUT = ""


def press(num):
    global INPUT
    INPUT = INPUT+str(num)
    equation.set(INPUT)


def calculate():
    global INPUT
    total = str(eval(INPUT))
    equation.set(total)
    INPUT = ''


def clear():
    global INPUT
    INPUT = ''
    equation.set(INPUT)


if __name__ == "__main__":
    root = Tk()

    mainframe = ttk.Frame(root, padding=10, width=300, height=500)
    mainframe.grid()

    equation = StringVar()

    input_field = Entry(mainframe, textvariable=equation)
    input_field.grid(columnspan=4, ipadx=70, pady=5)

    button_1 = ttk.Button(mainframe, text="9", command=lambda: press(9))
    button_1.grid(column=0, row=1)

    button_2 = ttk.Button(mainframe, text="8", command=lambda: press(8))
    button_2.grid(column=1, row=1)

    button_3 = ttk.Button(mainframe, text="7", command=lambda: press(7))
    button_3.grid(column=2, row=1)

    button_4 = ttk.Button(mainframe, text="6", command=lambda: press(6))
    button_4.grid(column=0, row=2)

    button_5 = ttk.Button(mainframe, text="5", command=lambda: press(5))
    button_5.grid(column=1, row=2)

    button_6 = ttk.Button(mainframe, text="4", command=lambda: press(4))
    button_6.grid(column=2, row=2)

    button_7 = ttk.Button(mainframe, text="3", command=lambda: press(3))
    button_7.grid(column=0, row=3)

    button_8 = ttk.Button(mainframe, text="2", command=lambda: press(2))
    button_8.grid(column=1, row=3)

    button_9 = ttk.Button(mainframe, text="1", command=lambda: press(1))
    button_9.grid(column=2, row=3)

    button_10 = ttk.Button(mainframe, text="0", command=lambda: press(0))
    button_10.grid(column=1, row=4)

    button_times = ttk.Button(mainframe, text="x", command=lambda: press('*'))
    button_times.grid(column=3, row=1)

    button_divide = ttk.Button(mainframe, text="/", command=lambda: press('/'))
    button_divide.grid(column=3, row=2)

    button_plus = ttk.Button(mainframe, text="+", command=lambda: press('+'))
    button_plus.grid(column=3, row=3)

    button_equals = ttk.Button(mainframe, text="=", command=calculate)
    button_equals.grid(column=3, row=4)

    button_clear = ttk.Button(mainframe, text="Clear", command=clear)
    button_clear.grid(column=0, row=4)

    root.mainloop()
