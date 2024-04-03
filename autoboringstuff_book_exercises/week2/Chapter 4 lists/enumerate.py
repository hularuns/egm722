supplies= ['pens', 'staplers', 'flamethrowers', 'binders']

#Loop will obtain the integer of index of items in the list.
# Each iteration of the enumerate() will return two values. 
# #The index of the item in the list and the item in the list itself.

for index, item in enumerate(supplies):
    print('Index ' +str(index) + ' in supplies is: ' + item)
    
# Same as this loop:
for index in range(len(supplies)):
    print('Index ' + str(index) + ' in supplies is: ' + supplies[index])
    
spam = 42
spam //= 3
print(spam)