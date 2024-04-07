#Data structure to model the player's inventory in a fantasy game.
# Write a function to display any possible inventory and display using pprint

# import pprint
import random
import time
import sys
invent = {'rope':1, 'gold coin': 42, 'arrow': 12, 'torch': 6, 'dagger': 1}
dragonLoot = ['gold coin', 'dwarf head', 'dagger', 'gold coin', 'gold coin', 'ruby']
loot = {}

#Gear
weapon = {'sword':{'stab': random.randint(3,6)}}
dragon = {'name': 'Elvarg', 'health': 100, 'defense': 3}

def PlayerPickup(loot):
    looting = True
    while looting == True and loot:
        print('Type which item you want to pick up')
        pickedItem = input().strip()

        if pickedItem in loot:
            invent[pickedItem] = loot[pickedItem] #adds item from loot to global invent
            del loot[pickedItem] # removes from loot
            print(f'{pickedItem} was picked up')
            print(f'The remaining items are left: {loot}')
        elif pickedItem.lower() == 'finished':
            print('You have walked away from your kill!')
            break
        else:
            print('This item was not dropped!')
        if not loot:
            print('All loot has been picked up or discarded.')
            break
        print(f'Your inventory is currently: {invent}')

#fight the monster
def battleMonster(monster):
    global loot # global reference
    monsterHealth = monster['health']
    attackDamage = weapon['sword']['stab']

    #fight goes down including input choices

    while monsterHealth > 0:
        print(f'{monster['name']} has {monsterHealth} left')
        monsterHealth -= attackDamage
        time.sleep(0.02)
    
        
    if monsterHealth <= 0:
        loot = {'Golden dung': 6, 'Potatoes': 3, 'Dragon bones': 1}
        print(f'{monster['name']} has been defeated!')
        print(f'{loot}')
        lootActive = input("Do you want to loot? y/n: ").lower().strip()
        if lootActive == 'y'.lower().strip():
            PlayerPickup(loot)





    


battleMonster(dragon) 



#battle



#If a dragon is looted.
""" 
def addToInventory(inventory, loot):
    for item in loot:
        inventory[item] = inventory.get(item, 0) + 1  # Increment the count if the item exists, else set it to 1
    return inventory

#displays inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, quantity in inventory.items():
        print(str(quantity) + ' ' + item)
        item_total += quantity
    print("Total number of items: " + str(item_total)) """

""" #For each item in the inventory dictionary, counts the inventory
#this way not as good
def displayInventory(inventory):
    itemTotal = 0
    for item in inventory:
        itemQuantity = inventory[item]
        itemTotal += itemQuantity
        print(str(inventory[item]) + ' ' + item)
    print('Total objects: ' + str(itemTotal))
 """
""" 
invent = addToInventory(invent, dragonLoot)
displayInventory(invent) """
