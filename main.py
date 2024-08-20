
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

def bla():
    g_code = ""
    print("something")
    text_area.insert(tk.INSERT, " ")
def generate_code():

    n = int(n_entry.get())
    l = float(l_entry.get())
    t = float(t_entry.get())
    o = float(o_entry.get())

    match t:
        case t if 0 < t <=1:
            fcut = 7650
        case t if 1 < t <=2:
            fcut = 5560
        case t if 2 < t <= 3:
            fcut = 3960
        case t if 3 < t <= 4:
            fcut = 2800
        case t if 4 < t <= 5:
            fcut = 1980
        case _:
            fcut = 1430

    g_code_entry = "G90 G17 G21 \nG54\n"

    g_code_body=""
    i = 0
    while i < n:
        g_code_body += f"G0X{l+o+i*l}\nM3\nG1A{360*(i+1)}F{fcut}\nM5\n"
        i+=1
    g_code_ending = "M30"
    g_code = f"{g_code_entry}{g_code_body}{g_code_ending}"
    text_area.insert(tk.INSERT,g_code)


##VIEWCONTROLLER
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Simple cut G-Code generator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=600, height=100)
canvas.grid(row=0, column=1)

#Labels
n_label = Label(text='n', font=12)
n_label.grid(row=1, column=0, sticky="E")
l_label = Label(text="interval length(mm)",font=12)
l_label.grid(row=2, column=0, sticky="E")
t_label = Label(text="thickness(mm)",font=12)
t_label.grid(row=3,  column=0, sticky="E")
o_label = Label(text="offset(mm)",font=12)
o_label.grid(row=4,  column=0, sticky="E")

# Entries
n_entry = Entry(width=35, font=12)
n_entry.insert(0,1)
n_entry.focus()
n_entry.grid(row=1, column=1, sticky='W')
l_entry = Entry(width=35,font=12)
l_entry.insert(0,10)
l_entry.grid(row=2, column=1,sticky='W')
t_entry = Entry(width=35,font=12)
t_entry.insert(0,1)
t_entry.grid(row=3, column=1,sticky='W')
o_entry = Entry(width=35,font=12)
o_entry.insert(0,2)
o_entry.grid(row=4, column=1,sticky='W')

#Buttons
generate_code_but = Button(text="Generate G-Code", width=36, command=generate_code)
generate_code_but.grid(row=1, column=1, sticky="E")
clear_code_but = Button(text="Clear", width=36, command=bla)
clear_code_but.grid(row=2, column=1, sticky="E")

#Output
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width= 80, height= 10, font=('Times New Roman', 12))
text_area.grid(column=1, columnspan=2)
window.mainloop()