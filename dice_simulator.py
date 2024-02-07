import tkinter as tk
from tkinter import scrolledtext
import random

def roll_dices():
    num_dices = int(num_dices_var.get())
    num_sides = int(num_sides_var.get())
    results = [random.randint(1, num_sides) for _ in range(num_dices)]
    total = sum(results)
    results_str = ", ".join(str(r) for r in results)

    history_text.config(state=tk.NORMAL)
    history_text.insert(tk.END, f"Dés: {results_str} | Total: {total}\n")
    history_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Simulateur de Lancer de Dés Avancé")

num_dices_var = tk.StringVar(value='1')
num_sides_var = tk.StringVar(value='6')

instructions = tk.Label(app, text="Nombre de dés et nombre de faces:")
instructions.pack()

frame = tk.Frame(app)
frame.pack()

num_dices_label = tk.Label(frame, text="Dés:")
num_dices_label.pack(side=tk.LEFT)
num_dices_entry = tk.Entry(frame, textvariable=num_dices_var, width=5)
num_dices_entry.pack(side=tk.LEFT)

num_sides_label = tk.Label(frame, text="Faces:")
num_sides_label.pack(side=tk.LEFT)
num_sides_entry = tk.Entry(frame, textvariable=num_sides_var, width=5)
num_sides_entry.pack(side=tk.LEFT)

roll_button = tk.Button(app, text="Lancer les dés", command=roll_dices)
roll_button.pack()

history_label = tk.Label(app, text="Historique des lancers:")
history_label.pack()

history_text = scrolledtext.ScrolledText(app, state='disabled', height=10)
history_text.pack()

app.mainloop()
