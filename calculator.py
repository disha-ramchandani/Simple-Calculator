from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=40, borderwidth=2)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(s):
    curr = e.get()
    e.delete(0, END)
    global equation
    equation = str(curr) + str(s)
    e.insert(0, equation)


def buttonClr():
    e.delete(0, END)


def calculate():
    temp = ''
    answer = 0.0
    for ch in equation:
        if ch == '+' or ch == '-' or ch == '/' or ch == 'x':
            answer = float(temp)
            temp = ''
        else:
            temp = temp + ch
    for ch in equation:
        if ch == '+':
            answer = answer + float(temp)
        elif ch == '-':
            answer = answer - float(temp)
        elif ch == '/':
            answer = answer / float(temp)
        elif ch == 'x':
            answer = answer * float(temp)
        else:
            continue
    return answer

def buttonPerc():
    n = e.get()
    ans = float(n) / 100
    e.delete(0, END)
    e.insert(0, ans)

def buttonEq():
    ans = calculate()
    e.delete(0, END)
    e.insert(0, ans)


button1 = Button(root, text='1', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("1")).grid(row=4, column=0)
button2 = Button(root, text='2', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("2")).grid(row=4, column=1)
button3 = Button(root, text='3', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("3")).grid(row=4, column=2)

button4 = Button(root, text='4', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("4")).grid(row=3, column=0)
button5 = Button(root, text='5', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("5")).grid(row=3, column=1)
button6 = Button(root, text='6', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("6")).grid(row=3, column=2)

button7 = Button(root, text='7', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("7")).grid(row=2, column=0)
button8 = Button(root, text='8', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("8")).grid(row=2, column=1)
button9 = Button(root, text='9', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("9")).grid(row=2, column=2)

button0 = Button(root, text='0', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click("0")).grid(row=5, column=0)
button_deci = Button(root, text='.', bg="black", fg="white", padx=40, pady=20, command=lambda: button_click(".")).grid(row=5, column=1)

button_clr = Button(root, text='CLR', bg="black", fg="white", padx=80, pady=20, command=buttonClr).grid(row=1, column=0, columnspan=2)
button_eq = Button(root, text='=', bg="black", fg="white", padx=86, pady=20, command=buttonEq).grid(row=5, column=2, columnspan=2)

button_add = Button(root, text='+', bg="black", fg="white", padx=39, pady=20, command=lambda: button_click("+")).grid(row=1, column=3)
button_sub = Button(root, text='-', bg="black", fg="white", padx=39, pady=20, command=lambda: button_click("-")).grid(row=2, column=3)
button_div = Button(root, text='/', bg="black", fg="white", padx=39, pady=20, command=lambda: button_click("/")).grid(row=3, column=3)
button_mult = Button(root, text='x', bg="black", fg="white", padx=39, pady=20, command=lambda: button_click("x")).grid(row=4, column=3)
button_percent = Button(root, text='%', bg="black", fg="white", padx=39, pady=20, command=buttonPerc).grid(row=1, column=2)

root.mainloop()
