#This counts the number of times a character appears within a string.
import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count) #using pretty print makes dictionary printing much tidier.


