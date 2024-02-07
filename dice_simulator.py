import tkinter as tk
from tkinter import ttk
import random
import itertools
import time

def update_dice_image(image_labels, images, num_dices, delay=0.1, iterations=10):
    for _ in range(iterations):
        for label in image_labels:
            image = next(images[random.randint(0, num_dices-1)])
            label.config(image=image)
        app.update()
        time.sleep(delay)

def roll_dice():
    num_dices = int(num_dices_spinbox.get())
    results = [random.randint(1, 6) for _ in range(num_dices)]
    update_dice_image(dice_image_labels, dice_images_iters, num_dices)
    dice_result.config(text=f"Résultats : {' '.join(str(r) for r in results)}")

app = tk.Tk()
app.title("Simulateur de Lancer de Dés Animé Avancé")

num_dices_var = tk.StringVar(value='1')
num_dices_spinbox = ttk.Spinbox(app, from_=1, to=6, textvariable=num_dices_var, width=5)
num_dices_spinbox.pack()

roll_button = tk.Button(app, text="Lancer les dés", command=roll_dice)
roll_button.pack()

dice_images = [[tk.PhotoImage(file=f'images/de_{j}_{i}.png') for i in range(1, 7)] for j in range(6)]
dice_image_labels = [tk.Label(app, image=dice_images[j][0]) for j in range(6)]
for label in dice_image_labels:
    label.pack(side=tk.LEFT)

dice_images_iters = [itertools.cycle(images) for images in dice_images]

dice_result = tk.Label(app, text="")
dice_result.pack()

app.mainloop()
