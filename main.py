
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import pyperclip


font_sd = ("Helvetica", "14", "bold")
def copy_text():
    text_to_copy = text_area.get("1.0", tk.END)
    pyperclip.copy(text_to_copy)
def clear_code():
    text_area.configure(state='normal')
    text_area.delete('1.0',tk.END)
def generate_code():

    n = int(n_entry.get())
    l = float(l_entry.get())
    t = float(t_entry.get())
    o = float(o_entry.get())
    fc = float(fcut_entry.get())
    if fc == 0:
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
    else:
        fcut = fc

    g_code_entry = "G90 G17 G21 \nG54\n"

    g_code_body=""
    i = 0
    while i < n:
        g_code_body += f"G0X{l+i*l+o*(1+i)}\nM3\nG1A{360*(i+1)}F{fcut}\nM5\n"
        i+=1
    g_code_ending = "M30"
    g_code = f"{g_code_entry}{g_code_body}{g_code_ending}"
    text_area.insert(tk.INSERT,g_code)
    text_area.configure(state='disabled')


##VIEWCONTROLLER
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Simple cut G-Code generator")
window.geometry('780x580')
#window.columnconfigure((0,1,2), weight=1)
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

img_tk = tk.PhotoImage(file="header_image2.png")
canvas = Canvas(width=750, height=80)
canvas.create_image(400,100,image=img_tk, anchor=S)
canvas.grid(row=0, column=0, columnspan=3)

#Labels
n_label = Label(text='Số lần cắt n', font=font_sd, bg=BACKGROUND_COLOR)
n_label.grid(row=1, column=0, sticky="E", pady=5)

l_label = Label(text="Chiều dài cắt L(mm)",font=font_sd, bg=BACKGROUND_COLOR)
l_label.grid(row=2, column=0, sticky="E", pady=5)

t_label = Label(text="Độ dày ống t(mm)",font=font_sd, bg=BACKGROUND_COLOR)
t_label.grid(row=3,  column=0, sticky="E", pady=5)

o_label = Label(text="Bù chều dài o(mm)",font=font_sd, bg=BACKGROUND_COLOR)
o_label.grid(row=4,  column=0, sticky="E", pady=5)

fcut_label = Label(text="Tốc độ cắt", font=("Helvetica", "9", "italic"), bg=BACKGROUND_COLOR,fg="#0D7C66")
fcut_label.grid(row=5, column=0, sticky="ES", pady=1)

# Infor ref
text_ref = ("Bảng tham chiếu tốc độ cắt\n"
            "   t(mm)            F\n"
            "   1               7650\n"
            "   2               5560\n"
            "   3               3960\n"
            "   4               2800\n"
            "   5               1980\n"
            "   6               1430\n"
            "Phần mềm đã tự động tính toán tốc độ dựa trên thông số t \n"
            "đã input.Tuy nhiên bạn có thể hiệu chỉnh tốc độ cắt\n"
            "trong field dưới đây.Lưu ý nhập 0 nếu muốn phần mềm \n"
            "tự tính toán.\n"
            )
ref_label = Label(text=text_ref, font=("Helvetica", "9", "italic"), bg=BACKGROUND_COLOR,fg="#0D7C66" )
ref_label.grid(row=5, column=0, columnspan=2, sticky="N", pady=5)

# Entries
n_entry = Entry(width=15, font=12)
n_entry.insert(0,1)
n_entry.focus()
n_entry.grid(row=1, column=1, sticky='W', pady=2)

l_entry = Entry(width=15,font=12)
l_entry.insert(0,10)
l_entry.grid(row=2, column=1,sticky='W', pady=2)

t_entry = Entry(width=15,font=12)
t_entry.insert(0,1)
t_entry.grid(row=3, column=1,sticky='W', pady=2)

o_entry = Entry(width=15,font=12)
o_entry.insert(0,2)
o_entry.grid(row=4, column=1,sticky='W', pady=2)

fcut_entry =  Entry(width=10, font=8)
fcut_entry.insert(0,0)
fcut_entry.grid(row=5, column=1, sticky='SW', pady=1)

#Buttons
generate_code_but = Button(text="Tạo G-Code",command=generate_code)
generate_code_but.grid( row=6,column=0,columnspan=2, sticky="WE")

clear_code_but = Button(text="Xóa", width=20, command=clear_code)
clear_code_but.grid(row=6, column=2, sticky="W", padx=10)

copy_but = Button(text="Sao chép", width=20, command=copy_text)
copy_but.grid(row=6, column=2, sticky="E", pady=10, padx=5)

#Output
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width= 30, height= 23, font=("Helvetica", "12"))
text_area.grid(row=1,column=2, rowspan=5, sticky="NS",pady=5, padx=10)
window.mainloop()