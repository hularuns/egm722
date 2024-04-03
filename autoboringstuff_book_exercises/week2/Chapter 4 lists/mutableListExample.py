spam = [0,1,2,3,4,5,6]

cheese = spam #The reference is being copied, but not the list  to cheese.

cheese[1] = 'Hello!' # This changes the list value (spam through the copied reference cheese)

print(spam)

print(cheese)