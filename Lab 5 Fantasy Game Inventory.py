# Name: Jose Alcala
# Date: 10/10/2023
# Course: CIS 188

# Description: Fantasy Game Inventory Management System

# CIS188_inventory.py

# Function to display the player's inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(str(count) + " " + item)   # shows how many of each item
        item_total += count
    print("Total number of items: " + str(item_total))


# Function to add items from loot into the inventory
def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1   # add +1 if item already exists
        else:
            inventory[item] = 1    # create new item with count 1
    print("Inventory updated!")
    return inventory


# ----- Main program -----
# starting items
stuff = {'rope': 1, 'gold coin': 42, 'dagger': 1}

# loot from dragon
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("The dragon has been vanquished! Looting...")
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
