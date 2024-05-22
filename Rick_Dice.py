import random


def dice_roll():
    greet = input("Welcome! Ready to roll? (Y/N): ").lower()
    while greet in ["yes", "y"]:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        print("Rolling...")
        print(f"You rolled {roll1} and {roll2}! A total of {total}!")

        greet = input("Do you want to roll again? (Y/N): ").lower()

    print("Thanks for playing!")


# Call the dice roll
dice_roll()
