import time
import sys

indent = 0 #variable to store how many spaces to indent by.
indentIncreasing = True #Whether the indentation is increasing or not. Default starts True.

try: 
    while True: #The main program loop.
        print('-' * indent, end='')
        print('********')
        time.sleep(0.1) #pause the loop for 0.1 seconds.
        if indentIncreasing:
            #increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False
        else:
            #Decrease the number of spaces
            indent = indent - 1
            if indent == 10:
                #Change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()