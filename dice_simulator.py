import tkinter as tk
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
    num_sides = 6
    result = random.randint(1, num_sides)
    update_dice_image(dice_image_label, itertools.cycle(dice_images))
    dice_result.config(text=f"Résultat : {result}")

app = tk.Tk()
app.title("Simulateur de Lancer de Dés Animé")

dice_images = [tk.PhotoImage(file=f'images/de_{i}.png') for i in range(1, 6)]
dice_image_label = tk.Label(app, image=dice_images[0])
dice_image_label.pack()

roll_button = tk.Button(app, text="Lancer le dé", command=roll_dice)
roll_button.pack()

dice_result = tk.Label(app, text="")
dice_result.pack()

app.mainloop()
