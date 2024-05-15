import random
import math

# Taking Inputs
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

# generating random number between the lower and upper
x = random.randint(lower, upper)

# Setting a fixed number of chances
chances = 5
print(f"\n\tYou've only {chances} chances to guess the integer!\n")

# Loop to handle guesses
for count in range(chances):
    # taking guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if x == guess:
        print(f"\n\tCongratulations! You guessed it in {count + 1} tries.\n")
        # Once guessed correctly, exit the loop
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If all chances are used without guessing correctly
else:
    print("\nThe number was:", x)
    print("\tBetter Luck Next time!")
