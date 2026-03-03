import random  # Import random module

while True:
    choice = input("Roll the dice? (y/n): ").lower()  # Take user input

    if choice == 'y':
        die1 = random.randint(1, 6)  # Generate random number between 1 and 6
        die2 = random.randint(1, 6)
        print(f"You rolled: ({die1}, {die2})")

    elif choice == 'n':
        print("Thank you for playing!") 
        break

    else:
        print("Invalid choice! Please enter 'y' or 'n'.")
