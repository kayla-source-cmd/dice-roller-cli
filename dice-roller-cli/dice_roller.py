import random

while True:
    roll = random.randint(1, 6)
    print(f"You rolled: {roll}")

    while True:
        choice = input("Roll again? (yes/no): ").lower().strip()

        if choice in ["y", "yes"]:
            break

        elif choice in ["n", "no"]:
            print("Thanks for playing!")
            exit()

        else:
            print("Invalid choice! Enter yes or no.")