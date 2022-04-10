import tkinter as tk
import tkcalendar as tkc
from tkinter import ttk
import os.path
import tkinter.messagebox as mb

check_file = os.path.exists('calendar.txt')
if not check_file:
    try:
        file = open("calendar.txt", "w", encoding="utf-8")
    except FileNotFoundError:
        print("Файл невозможно создать!")


def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)


def save_user():
    try:
        file = open("calendar.txt", "a", encoding="utf-8")
    except FileNotFoundError:
        print("Файл не найден!")
    fio = entry1.get()
    bday = entry2.get()
    tel = entry3.get()

    error = False

    if fio == "":
        error = True

    if error:
        mb.showerror("Ошибка заполнения", "Вы не ввели ФИО")
    else:
        file.write(fio + "#" + bday + "#" + tel + "\n")
        tree.insert("", tk.END, values=(fio, bday, tel))


window = tk.Tk()
window.title("Дни рождения друзей")
window.geometry("450x400")
window.resizable(False, False)

frame = tk.Frame()
frame.pack()

label0 = tk.Label(master=frame, text="")
label0.grid(row=0, column=0)

label1 = tk.Label(master=frame, text="ФИО: ")
entry1 = tk.Entry(master=frame)
label1.grid(row=1, column=0, sticky="e")
entry1.grid(row=1, column=1, sticky="w e")

label2 = tk.Label(master=frame, text="Дата рождения: ")
entry2 = tkc.DateEntry(master=frame)
label2.grid(row=2, column=0, sticky="e")
entry2.grid(row=2, column=1, sticky="w e")

label3 = tk.Label(master=frame, text="Номер телефона: ")
entry3 = tk.Entry(master=frame)
label3.grid(row=3, column=0, sticky="e")
entry3.grid(row=3, column=1,  sticky="w e")

button1 = tk.Button(master=frame, text="Сохранить", command=save_user)
button1.grid(row=4, column=0, sticky="e", pady=10, padx=10)
button2 = tk.Button(master=frame, text="Очистить", command=clear)
button2.grid(row=4, column=1, sticky="w", pady=10, padx=10)

tree = ttk.Treeview(master=frame, show="headings",)
tree["columns"] = ("one", "two", "three")
tree.column("one", width=170)
tree.column("two", width=100)
tree.column("three", width=100)

tree.heading("one", text="ФИО")
tree.heading("two", text="День рождения")
tree.heading("three", text="Телефон")

try:
    file = open("calendar.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Файл не найден!")

for ff in file:
    ff = ff.split("#")
    tree.insert("", tk.END, values=(ff[0], ff[1], ff[2]))

tree.grid(row=5, column=0, columnspan=2)
vsb = ttk.Scrollbar(master=frame, orient="vertical", command=tree.yview)
vsb.grid(row=5, column=3, sticky="NS")
tree.configure(yscrollcommand=vsb.set)

window.mainloop()
