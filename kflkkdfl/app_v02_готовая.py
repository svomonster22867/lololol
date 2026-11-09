# Приложение «Приём заявок», версия 0.2.1 (готовая после исправлений)

from tkinter import *
from tkinter import ttk
from datetime import datetime
from pathlib import Path

LIMIT = 10          # по требованиям: максимум 10 заявок
count = 0           # сколько заявок принято
STATUSES = ["Новая", "В работе", "Готово"]
status_index = 0

def accept():
    global count
    count = count + 1
    label_count["text"] = count
    label_date["text"] = "Принято: " + datetime.now().strftime("%d.%m.%Y %H:%M")
    if count >= LIMIT:
        label_count["text"] = "Лимит: " + str(count)
        btn_accept["state"] = "disabled"

def reset():
    global count
    count = 0
    label_count["text"] = count
    btn_accept["state"] = "normal"
    label_date["text"] = "Принято: —"

def change_status():
    global status_index
    status_index = (status_index + 1) % len(STATUSES)
    label_status["text"] = "Статус: " + STATUSES[status_index]

window = Tk()
window.title("Приём заявок")
window.geometry("300x420")

logo = PhotoImage(file=str(Path(__file__).with_name("logo.png")))
picture = Label(image=logo)
picture.pack()

label_title = Label(text="Количество заявок:")
label_title.pack()

label_count = Label(text="0", fg="black")
label_count.pack()

label_date = Label(text="Принято: —")
label_date.pack()

label_status = Label(text="Статус: Новая")
label_status.pack()
btn_status = ttk.Button(text="Сменить статус", command=change_status)
btn_status.pack(pady=5)

btn_accept = ttk.Button()
btn_accept.pack(pady=5)
btn_accept["text"] = "Принять заявку"
btn_accept["command"] = accept

btn_reset = ttk.Button()
btn_reset.pack(pady=5)
btn_reset["text"] = "Сбросить"
btn_reset["command"] = reset

btn_accept["width"] = 20
btn_reset["width"] = 20

window.mainloop()
