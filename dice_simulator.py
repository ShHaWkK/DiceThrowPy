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

