myPets = ['Zophie', 'Pooka', 'Fat-tail']

print('Enter a pet name:')
name = input()

if name not in myPets:
    petsString = ', '.join(myPets) #Converts myPets into a string
    print('I do not have a pet names ' + name + '.' +' The only pets i own are ' + petsString + '.')
else:
    print(name + ' is my pet.')