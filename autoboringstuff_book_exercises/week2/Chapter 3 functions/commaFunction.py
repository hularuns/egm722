""" Write a function that takes a list value as an argument and returns a string with all the items 
separated by a comma and a space, with and inserted before the last item. For example, passing the 
previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function
should be able to work with any list value passed to it. Be sure to test the case where an empty
list [] is passed to your function. """

spam = ["apples", "bananas", "tofu", "cats"]
print(", ".join(spam[:-1]) + f" and {spam[-1]}")

def commaFunction(listItem):
    commaList = []
    commaString = ""
    for item in listItem:
        commaList = commaList + [item]
    for i in range(len(listItem)):
        if i < len(listItem) - 1:
            commaString += listItem[i] + ", "
        else:
            commaString += "and " + listItem[i]

    print(commaString)


commaFunction(spam)

""" 
def commaFunction(listItem):
    commaList = []
    commaString = ""
    for item in listItem:
        commaList = commaList + [item]
    for i in range(len(listItem)):
        if i < len(listItem) - 1:
            commaString += listItem[i] + ", "
        else:
            commaString += "and " + listItem[i]

    print(commaString) """
