import tkinter as tk
from tkinter import ttk
import random
import itertools
import time


def roll_dice():
    num_dices = int(num_dices_spinbox.get())
    results = [random.randint(1, 6) for _ in range(num_dices)]
    show_dice_animations(results)
    update_statistics(results)
    update_history(results)


def show_dice_animations(results):
    for _ in range(10):  # Nombre d'itérations pour l'animation
        for label in dice_image_labels:
            label.config(image=random.choice(dice_images))
        app.update()
        time.sleep(0.1)

    for label, result in zip(dice_image_labels, results):
        label.config(image=dice_images[result - 1])


def update_statistics(results):
    total = sum(results)
    avg = total / len(results) if results else 0
    stats_label.config(text=f"Total: {total}, Moyenne: {avg:.2f}")


def update_history(results):
    history.insert(tk.END, f"{results} (Total: {sum(results)})\n")
    history.see(tk.END)


def setup_dice_labels(num_dices):
    for label in dice_image_labels:
        label.pack_forget()
    dice_image_labels.clear()

    for _ in range(num_dices):
        label = tk.Label(dice_frame, image=dice_images[0])
        label.pack(side=tk.LEFT)
        dice_image_labels.append(label)


app = tk.Tk()
app.title("Simulateur de Lancer de Dés Animé Avancé")

style = ttk.Style(app)
style.theme_use('clam')  # Choix d'un thème

num_dices_var = tk.StringVar(value='1')
num_dices_spinbox = ttk.Spinbox(app, from_=1, to=6, textvariable=num_dices_var, width=5,
                                command=lambda: setup_dice_labels(int(num_dices_spinbox.get())))
num_dices_spinbox.pack()

roll_button = ttk.Button(app, text="Lancer les dés", command=roll_dice)
roll_button.pack()

dice_frame = ttk.Frame(app)
dice_frame.pack()

dice_images = [tk.PhotoImage(file=f'images/de_{i}.png') for i in range(1, 7)]
dice_image_labels = []
setup_dice_labels(int(num_dices_spinbox.get()))

stats_label = ttk.Label(app, text="", font=("Helvetica", 14))
stats_label.pack()

history_label = ttk.Label(app, text="Historique des lancers :", font=("Helvetica", 14))
history_label.pack()

history = tk.Text(app, height=5, width=30)
history.pack()

app.mainloop()
