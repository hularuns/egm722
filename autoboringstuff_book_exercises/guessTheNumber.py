# Number guessing game
import random

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
# ask the player to guess up to 6 times.
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess it too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # this condition is the correct guess!
    # If statement to print the number if the player got it right or not.
if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
