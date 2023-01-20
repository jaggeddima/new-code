from tkinter import *
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Выход из идиота :)",
                              "Выходи!"):
        tk.destroy()

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Лол")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=700, height=700,
                bg="red",  highlightthickness=0)
canvas.pack()

canvas.create_oval(120, 120,
                   300, 300,
                   fill="white")

tk.mainloop()


