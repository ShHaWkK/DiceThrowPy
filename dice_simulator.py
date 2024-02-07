import tkinter as tk
import random


def roll_dice():
    num_sides = sides_var.get()
    if not num_sides:
        num_sides = 6
    else:
        num_sides = int(num_sides)

    roll = random.randint(1, num_sides)
    result_label.config(text=f"Résultat : {roll}")


app = tk.Tk()
app.title("Simulateur de Lancer de Dés")

sides_var = tk.StringVar()

instructions = tk.Label(app, text="Entrez le nombre de faces du dé:")
instructions.pack()

sides_entry = tk.Entry(app, textvariable=sides_var)
sides_entry.pack()

roll_button = tk.Button(app, text="Lancer le dé", command=roll_dice)
roll_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
