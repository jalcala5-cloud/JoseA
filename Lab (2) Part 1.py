#Lab 2 Part 1
#Name: Jose Serafin Alcala Moreno
#Date: 8//2025
#Class: CIS188


# Ask for the user's name
username = input("Please enter your name: ")

# Ask for the user's age
user_age = int(input("Hello, " + username + "! How old are you? "))

# Ask about food preference
dinner = input("Do you like pizza or pasta? ")

# First decision: based on age
if user_age >= 18:
    # Second decision: based on dinner choice
    if dinner.lower() == 'pasta':
        print("Awesome, " + username + "! We're going to Olive Garden and ordering " + dinner + " tonight!")
    elif dinner.lower() == 'pizza':
        print("I know a fancy " + dinner + " place with a special that includes drinks and a side!")
    else:
        print("I've never made " + dinner + " before, but we can go get groceries and make it!")
else:
    print("Sorry, " + username + ", I have homework that's due tomorrow, we have to ask my parents before we can get " + dinner + " tonight.")

# End of program message
print("Thanks for dinner, " + username + "!")