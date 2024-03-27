import random

# pick a random number for the user to guess. Changed to 1-20 to match instructions
rand = random.randint(1, 20)
# print(rand) #uncomment to debug
print('Guess a number between 1 and 20.')
guess = int(input())  # number needs to be an integer

while guess != rand:  # if the guess is not equal to the random number, you have to guess again
    if guess == rand:  # Tells the user if they are correct
        print('Correct!')
    elif guess < rand:  # Tells the user if too low
        print('Too low. Guess again.')
    else:  # if the guess is too high
        print('Too high. Guess again.')

    print('Enter a new guess: ')
    guess = int(input())

print('You got it! The number was {}'.format(rand))
