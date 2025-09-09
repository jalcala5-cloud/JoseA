# Name: <Jose Alcala> 
# Date: <6/19/2024>
# Class: CIS 188
# Description: This program computes the Collatz sequence for a given positive integer.

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

def main():
    print("Welcome to the Collatz Sequence calculator.")
    user_input = int(input("Please enter a positive number: "))
    
    while user_input != 1:
        user_input = collatz(user_input)

if __name__ == "__main__":
    main()
