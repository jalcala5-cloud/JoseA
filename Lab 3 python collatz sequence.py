# Name: [Jose Alcala]
# Date: [9/18/2025]
# Class:[CIS 188]

 # Description: This program computes the Collatz sequence for a given positive integer.

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print("Welcome to the Collatz Sequence calculator.")
num = int(input("Please enter a positive number:\n"))

sequence = [num]  # List to store the sequence

while num != 1:
    num = collatz(num)
    sequence.append(num)

print("Here is the full Collatz sequence:")
print(sequence)
print(f"It took {len(sequence) - 1} steps to reach 1.")
