from tkinter import *
from tkinter import Entry

root = Tk()
Income_exercise = Entry(root, width=35, borderwidth=5)
Income_exercise.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


class outcome:
    def __init__(self, firstnum, operator, othernum):
        self.firstnum = firstnum
        self.operator = operator
        self.othernum = othernum

    def outpet0(self):
        if operator == '+':
            Income_exercise.insert(0, str(self.firstnum + self.othernum))
        elif operator == '-':
            Income_exercise.insert(0, str(self.firstnum - self.othernum))
        elif operator == '*':
            Income_exercise.insert(0, str(self.firstnum * self.othernum))
        elif operator == '/':
            Income_exercise.insert(0, str(self.firstnum / self.othernum))
        elif operator == '^':
            Income_exercise.insert(0, str(pow(self.firstnum, self.othernum)))


def button_click(number):
    current = Income_exercise.get()
    Income_exercise.delete(0, END)
    Income_exercise.insert(0, str(current) + str(number))


def button_clear1():
    Income_exercise.delete(0, END)


def button_division1():
    first_number = Income_exercise.get()
    global operator
    operator = "/"
    global f_num
    f_num = int(first_number)
    Income_exercise.insert(f_num, operator)


def button_add1():
    first_number = Income_exercise.get()
    global operator
    operator = "+"
    global f_num
    f_num = int(first_number)
    Income_exercise.insert(f_num, operator)


def button_multiplication1():
    first_number = Income_exercise.get()
    global operator
    operator = "*"
    global f_num
    f_num = int(first_number)
    Income_exercise.insert(f_num, operator)


def button_subtract1():
    first_number = Income_exercise.get()
    global operator
    operator = "-"
    global f_num
    f_num = int(first_number)
    Income_exercise.insert(f_num, operator)


def button_power1():
    first_number = Income_exercise.get()
    global operator
    operator = "^"
    global f_num
    f_num = int(first_number)
    Income_exercise.insert(f_num, operator)

def button_equal2():
    current_num = Income_exercise.get()
    currently_num = current_num.rfind(operator)
    current_num = int(current_num[currently_num + 1:])
    Income_exercise.delete(0, END)
    outcome1 = outcome(f_num, operator, current_num)
    outcome1.outpet0()


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_equal = Button(root, text="=", padx=90, pady=20, command=lambda: button_equal2())
button_clear = Button(root, text="clear", padx=30, pady=20, command=lambda: button_clear1())
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: button_add1())
button_subtraction = Button(root, text="-", padx=40, pady=20, command=lambda: button_subtract1())
button_division = Button(root, text="/", padx=40, pady=20, command=lambda: button_division1())
button_multiplication = Button(root, text="*", padx=40, pady=20, command=lambda: button_multiplication1())
button_power = Button(root, text="^", padx=40, pady=20, command=lambda: button_power1())


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_power.grid(row=4, column=1)
button_multiplication.grid(row=4, column=2)

button_subtraction.grid(row=5, column=0)
button_add.grid(row=5, column=1)
button_division.grid(row=5, column=2)

button_equal.grid(row=6, column=1, columnspan=3)
button_clear.grid(row=6, column=0)


root.mainloop()
