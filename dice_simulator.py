import random

def roll_dice(num_sides=6):
    """Fonction pour simuler le lancer d'un dé à 'num_sides' faces."""
    return random.randint(1, num_sides)

def main():
    num_sides = input("Entrez le nombre de faces du dé (6 par défaut): ")
    if not num_sides:
        num_sides = 6
    else:
        num_sides = int(num_sides)

    roll = roll_dice(num_sides)
    print(f"Résultat du lancer de dé: {roll}")

if __name__ == "__main__":
    main()
