# Name: <Jose Alcala>
# Date: <09/09/2025>
# Class: CIS 188

# Description: This program simulates a dinner adventure in the Mushroom Kingdom.

import random

def mario_dinner():
    name = input("Who’s joining the dinner adventure in the Mushroom Kingdom?\n")
    print(f"It's-a me, {name}! How old are you?")
    age = input()  # Not used but part of interaction

    food = input("Do you prefer pizza or pasta, or something else entirely?\n").strip().lower()

    if food == "pizza":
        print(f"Mamma mia! Sorry {name}, Bowser’s causing trouble — we have to rescue Toad before we can eat pizza!")
    elif food == "pasta":
        print(f"Wahoo! {name}, we’re off to Princess Peach’s castle for some magical pasta!")
    else:
        print(f"Interesting choice, {name}... I’ve never had {food} in the Mushroom Kingdom, but let’s try making it with Yoshi!")

    yum_times = random.randint(3, 7)
    for i in range(yum_times):
        print("🍝 Yum!")

def main():
    print("🌟 Welcome to Super Mario Dinner Adventure! 🌟")
    
    while True:
        mario_dinner()
        again = input("\nDoes another character want to join the dinner quest? (Type 'No' to quit)\n").strip().lower()
        if again == "no":
            print("Thanks for joining us! See you next time in the Mushroom Kingdom! 🍄")
            break
        else:
            print("\n🔁 Loading next guest...\n")

if __name__ == "__main__":
    main()

