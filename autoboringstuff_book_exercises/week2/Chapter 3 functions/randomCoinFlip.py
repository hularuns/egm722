#function to show how many times H or T appear in 6 or more sequence

import random

def countStreak(flips):
    # holding variables
    numberOfStreaks = 0 
    flipList = []
    streakLength = 0
    lastFlip = None
    #Input the number to check by
    print('Input the number of flips in a row to check for')
    streakThreshold = input(int())
    
    for flip in range(flips):
        randomFlip = random.randint(0,1)
        if randomFlip == 0:
            flipList += ['Tails']
        elif randomFlip == 1:
            flipList += ['Heads']

        # if randomFlip is equal last flip it adds to the streakLength counter3
        if randomFlip == lastFlip:
            streakLength += 1
        else:
            #consecutive streak now broken. if hits thresold -> add to number of streak. regardless of this, reset styreak length to 1
            if streakLength >= int(streakThreshold):
                numberOfStreaks += 1  
            streakLength = 1  # Reset streak length for a new streak
            

        lastFlip = randomFlip


    print(f'\nWhen flipping a coin {flips} times, there are a streak of {numberOfStreaks} flips {streakThreshold} times in a row. \n')

    #print(flipList)
    
    flip
    
    
countStreak(200000)
