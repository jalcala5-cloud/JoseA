# Name: Jose Alcala
# Date: 6/12/2024
# Class: CIS 188

# Description: This program simulates coin flips to determine the
# Simulate flipping a coin 100 times, and check if there are
# 6 heads or tails in a row. Repeat the experiment 10,000 times to
# estimate the probability of getting a streak of 6.

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
	# Create a list of 100 'heads' or 'tails' values.
	flipList = []
	for i in range(100):
		flipList.append(random.choice(['H', 'T']))

	# Check for streaks of 6 heads or tails in a row.
	streak = 1
	for i in range(1, len(flipList)):
		if flipList[i] == flipList[i-1]:
			streak += 1
			if streak == 6:
				numberOfStreaks += 1
				break
		else:
			streak = 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))