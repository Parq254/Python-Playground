import tkinter as tk
from tkinter import *

app = tk.Tk()
app.geometry('170x230')
app.title('Calculator')
app.maxsize(170, 230)
app.minsize(170, 230)
ent = Entry(app, width=16, borderwidth=3, relief=RIDGE)
ent.grid(pady=10, row=0, sticky='w', padx=15)


def delete():
    a = ent.get()
    ent.delete(first = len(a) - 1, last='end')


def fresult():
    if ent.get() == '':
        pass
    elif ent.get()[0] == '0':
        ent.delete(0, 'end')
        c_res = ent.get()
        c_res = eval(c_res)
        clearf()
        ent.insert = ('end', c_res)


def clearf():
    ent.delete(0, 'end')


clean = Button(app, text='c', width=2, command=clearf, bg='gray', fg='white', relief=RIDGE)
clean.grid(row=0, sticky='w', padx=125)
char_nine = Button(text='9', width='2', command=lambda: ent.insert('end', '9'), borderwidth=3, relief=RIDGE)
char_nine.grid(row=1, sticky='w', padx=15)
char_eight = Button(text='8', width='2', command=lambda: ent.insert('end', '8'), borderwidth=3, relief=RIDGE)
char_eight.grid(row=1, sticky='w', padx=45)
char_seven = Button(text='7', width='2', command=lambda: ent.insert('end', '7'), borderwidth=3, relief=RIDGE)
char_seven.grid(row=1, sticky='w', padx=75)
char_plus = Button(app, text='+', width='2', command=lambda: ent.insert('end', '+'), borderwidth=3, relief=RIDGE)
char_plus.grid(row=1, sticky='e', padx=125)
char_six = Button(text='6', width='2', command=lambda: ent.insert('end', '6'), borderwidth=3, relief=RIDGE)
char_six.grid(row=2, sticky='w', padx=15, pady=5)
char_five = Button(text='5', width='2', command=lambda: ent.insert('end', '5'), borderwidth=3, relief=RIDGE)
char_five.grid(row=2, sticky='w', padx=45, pady=5)
char_four = Button(text='4', width='2', command=lambda: ent.insert('end', '4'), borderwidth=3, relief=RIDGE)
char_four.grid(row=2, sticky='w', padx=75, pady=5)
char_minus = Button(app, text='-', width='2', command=lambda: ent.insert('end', '-'), borderwidth=3, relief=RIDGE)
char_minus.grid(row=2, sticky='e', padx=125, pady=5)
char_three = Button(text='3', width='2', command=lambda: ent.insert('end', '3'), borderwidth=3, relief=RIDGE)
char_three.grid(row=3, sticky='w', padx=15, pady=5)
char_two = Button(text='2', width='2', command=lambda: ent.insert('end', '2'), borderwidth=3, relief=RIDGE)
char_two.grid(row=3, sticky='w', padx=45, pady=5)
char_one = Button(text='1', width='2', command=lambda: ent.insert('end', '1'), borderwidth=3, relief=RIDGE)
char_one.grid(row=3, sticky='w', padx=75, pady=5)
char_multiply = Button(app, text='*', width='2', command=lambda: ent.insert('end', '*'), borderwidth=3, relief=RIDGE)
char_multiply.grid(row=3, sticky='e', padx=125, pady=5)
char_zero = Button(text='0', width='2', command=lambda: ent.insert('end', '0'), borderwidth=3, relief=RIDGE)
char_zero.grid(row=4, sticky='w', padx=15, pady=5)
char_double_zero = Button(text='00', width='2', command=lambda: ent.insert('end', '00'), borderwidth=3, relief=RIDGE)
char_double_zero.grid(row=4, sticky='w', padx=45, pady=5)
char_dot = Button(text='.', width='2', command=lambda: ent.insert('end', '.'), borderwidth=3, relief=RIDGE)
char_dot.grid(row=4, sticky='w', padx=75, pady=5)
char_divide = Button(app, text='/', width='2', command=lambda: ent.insert('end', '/'), borderwidth=3, relief=RIDGE)
char_divide.grid(row=4, sticky='e', padx=125, pady=5)
result = Button(app,text='=', width='2', command=fresult, bg='gray', fg='white',borderwidth=3,relief=RIDGE)
result.grid(row=5, sticky='w', padx=15, pady=5)
char_modulus = Button(app, text='%', width='2', command=lambda: ent.insert('end', '%'), borderwidth=3, relief=RIDGE)
char_modulus.grid(row=5, stick='e', padx=125, pady=5)
delete = Button(text='del', width='2', command=delete, borderwidth=3, relief=RIDGE)
delete.grid(row=5, sticky='w', padx=80, pady=5)

app.mainloop()







