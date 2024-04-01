# function with one parameter for sequence


#Shoul return a sequence which ends up at 1.
def collatz(number):
        #if number is EVEN
        if number % 2 == 0:
            result = number // 2
        # number is ODD
        elif number % 2 == 1:
            result = 3 * number + 1
        print(result)
        return(result)

#Iterating collatz sequenced
print('Enter a number')

#try loop for the valueerror to print error if it's int or not
try:
    #while loop which returns a new value which is iterated on by the collatz function
    number = int(input())
    while number > 1:
        number = collatz(number)
        #print(number) #can have this here instead of within collatz function
except ValueError:
    print('Input a valid integer')
