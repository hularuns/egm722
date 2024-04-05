allGuests = {'Alice':{'apples': 5, 'pretzels':12},
             'Bob':{'ham sandwiches': 3, 'apples':2},
             'Carol':{'cups': 3, 'apple pies': 1}}
# Sums together all the individual items brought, where multiple people bring the samething or not

def totalBrought(guests, item):
    numBrought = 0
    for eachGuest, inventory in guests.items():
        numBrought = numBrought + inventory.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))