# Name: Jose Alcala
# Date: 09/30/2025
# Class: CIS188

# Description: This program simulates flipping a coin 100 times and checks for streaks of 6 heads or tails in a row.


import random


numberOfStreaks = 0 # Keeps track of how many streaks we've found


for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')


    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1
    hasStreak = False
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            streak += 1
            if streak == 6:
                hasStreak = True
                break
        else:
            streak = 1


    if hasStreak:
        numberOfStreaks += 1


print('Chance of streak: %s%%' % (numberOfStreaks / 100))
