
# fantasy game inventory

stuff = {'arrow':12, 'gold coin':42, 'rope':1, 'torch':6, 'dagger':1}
dragon_loot = ['dragon skull', 'dragon bone', 'alduin\'s greatsword', 'ruby', 'emerald', 'gold coin', 'gold coin', 'dragon bone', 'dragon bone', 'the elder scroll']

# display the user's inventory
def displayInventory(inventory):
    item_total = 0
    for i, j in inventory.items():
        print(str(j) + ' ' + i)
        item_total += j
    print('total number of items is ' + str(item_total))

# add loot to the users inventory
def addToInventory(inventory, addedItems):
    for i in addedItems:
            inventory.setdefault(i, 0)
            inventory[i] += 1

addToInventory(stuff, dragon_loot)
displayInventory(stuff)