
import tkinter as tk
from tkinter import * 
exp=""
def click(s):
    global exp
    exp=exp+str(s)
    expression.set(exp)

def calculate():
    try:
        global exp
        total = str(eval(exp))
        expression.set(total)
        exp = ""
    except:
        expression.set(" error ")
        exp = ""

def clear():
    global exp
    exp = ""
    expression.set("")

def delete():
    global exp
    exp=exp[0:len(exp)-1]
    expression.set(exp)


calculator = tk.Tk()
calculator.title("Calculator")
calculator.geometry("200x250")

expression=StringVar()

button1 = Entry(calculator,textvariable=expression,width=5)
button1.grid(columnspan=4,ipadx=75,ipady=8)

button2 = Button(calculator, text=' CE ', command=delete, height=2, width=5)
button2.grid(row=2, column=0)

button3 = Button(calculator, text='AC', command=clear, height=2, width=5)
button3.grid(row=2, column=1)

button4 = Button(calculator, text='Ans',command=calculate, height=2, width=5)
button4.grid(row=6, column=3,padx=3,pady=1)

button5 = Button(calculator, text=' ^ ', command=lambda: click('**'), height=2, width=5)
button5.grid(row=2, column=2,padx=3,pady=1)
 
button6 = Button(calculator, text=' / ',command=lambda: click('/'), height=2, width=5)
button6.grid(row=2, column=3,padx=3,pady=1)

button7 = Button(calculator, text=' 7 ', bg="silver",command=lambda: click(7), height=2, width=5)
button7.grid(row=3, column=0,padx=3)
 
button8 = Button(calculator, text=' 8 ', bg="silver", command=lambda: click(8), height=2, width=5)
button8.grid(row=3, column=1,padx=3)
 
button9 = Button(calculator, text=' 9 ', bg="silver", command=lambda: click(9), height=2, width=5)
button9.grid(row=3, column=2,padx=3)
 
button10 = Button(calculator, text=' * ',command=lambda: click('*'), height=2, width=5)
button10.grid(row=3, column=3,padx=3)

button11 = Button(calculator, text=' 4 ', bg="silver", command=lambda: click(4), height=2, width=5)
button11.grid(row=4, column=0,padx=3,pady=1)
 
button12 = Button(calculator, text=' 5 ', bg="silver", command=lambda: click(5), height=2, width=5)
button12.grid(row=4, column=1,padx=3,pady=1)
 
button13 = Button(calculator, text=' 6 ', bg="silver", command=lambda: click(6), height=2, width=5)
button13.grid(row=4, column=2,padx=3,pady=1)
 
button14 = Button(calculator, text=' - ',command=lambda: click('-'), height=2, width=5)
button14.grid(row=4, column=3,padx=3,pady=1)


button15 = Button(calculator, text=' 1 ', bg="silver", command=lambda: click(1), height=2, width=5)
button15.grid(row=5, column=0,padx=3,pady=1)
 
button16 = Button(calculator, text=' 2 ', bg="silver", command=lambda: click(2), height=2, width=5)
button16.grid(row=5, column=1,padx=3,pady=1)
 
button17 = Button(calculator, text=' 3 ', bg="silver", command=lambda: click(3), height=2, width=5)
button17.grid(row=5, column=2,padx=3,pady=1)
 
button18 = Button(calculator, text=' + ',command=lambda: click('+'), height=2, width=5)
button18.grid(row=5, column=3,padx=3,pady=1)

button19 = Button(calculator, text=' ', bg="silver", height=2, width=5)
button19.grid(row=6, column=0,padx=3,pady=1)
 
button20 = Button(calculator, text=' 0 ', bg="silver",command=lambda: click(0), height=2, width=5)
button20.grid(row=6, column=1,padx=3,pady=1)
 
button21 = Button(calculator, text=' . ', command=lambda: click('.'), height=2, width=5)
button21.grid(row=6, column=2,padx=3,pady=1)
 
calculator.mainloop()