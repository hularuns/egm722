#Data structure to model the player's inventory in a fantasy game.
# Write a function to display any possible inventory and display using pprint

# import pprint
invent = {'rope':1, 'gold coin': 42, 'arrow': 12, 'torch': 6, 'dagger': 1}
dragonLoot = ['gold coin', 'dwarf head', 'dagger', 'gold coin', 'gold coin', 'ruby']




#If a dragon is looted.

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
    print("Total number of items: " + str(item_total))

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

invent = addToInventory(invent, dragonLoot)
displayInventory(invent)
