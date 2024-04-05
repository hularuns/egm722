picnicItems = {"apples": 5, "cups": 2}
print("I am bringing " + str(picnicItems.get("cups", 0)) + " cups")

print("I am bringing " + str(picnicItems.get("eggs", 0)) + " eggs")

#using the setdefault() method to show a key if it doesn't already have a value

if 'color' not in picnicItems:
    picnicItems['color'] = 'orange'

#using setdefault lets you do something like below

spam = {'name': 'Pooka', 'age': 5, 'name': 'Joey', 'age':'5'}
spam.setdefault('color', 'black') #adds color: black to all dictionary items

print(spam)
