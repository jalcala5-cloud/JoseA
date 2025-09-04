#Lab 2 part 2 
#Name: Jose Serafin Alcala Moreno
#Date: 8//2025
#Class: CIS188


import random

while True:
    name = input("Please enter your name:\n")
    print(f"Hello, {name}! How old are you?")
    age = input()

    food = input("Do you like pizza or pasta?\n").lower()

    if food == "pizza":
        print(f"Sorry, {name}, I have homework that's due tomorrow, we have to ask my parents before we can get pizza tonight.\n")
    elif food == "pasta":
        print(f"Awesome, {name}! We're going to Olive Garden and ordering pasta tonight!")
    else:
        print(f"I've never heard of {food} but we can go get groceries and make it!")

    # Print "Yum" a random number of times between 3 and 7 (to match sample)
    yum_count = random.randint(3, 7)
    for _ in range(yum_count):
        print("Yum")

    again = input("Does someone else want to go to dinner?\n").lower()
    if again == "no":
        print(f"Thanks for dinner, {name}!")
        break
    print()
