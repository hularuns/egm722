import random


# Magic 8 ball function answers
def magic8BallAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return " It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"


r = random.randint(
    1, 9
)  # created a random number of 1 to 9 to put into magic 8ball function

fortune = magic8BallAnswer(r) #calls the magic8ball function
print(fortune)
