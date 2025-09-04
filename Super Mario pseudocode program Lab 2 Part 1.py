# Name: Jose Alcala
# Date: 9/02/2025
# Class: CIS188

# Mario Adventure pseudocode program


# Super Mario Adventure Game

# Get the user input

# Super Mario Adventure Game

# Get user input
print("Welcome to the Super Mario Adventure!")
name = input("What is your name? ")

# Ask which character to play
character_choice = input(f"Hello, {name}! Do you want to play as Mario or Luigi? ").lower()

# Ask where the player wants to go
location_choice = input("Where would you like to go: castle, forest, or underground? ").lower()

# Start the adventure
print("\n--- Your Adventure Begins! ---\n")

if character_choice == "mario":
    if location_choice == "castle":
        print(f"{name}, you play as Mario and storm Bowser's castle with fireballs blazing!")
    elif location_choice == "forest":
        print(f"{name}, as Mario, you run through the spooky forest dodging Goombas and finding power-ups!")
    elif location_choice == "underground":
        print(f"{name}, you explore the underground pipes and discover a hidden stash of coins!")
    else:
        print(f"That place doesn't exist in the Mushroom Kingdom, {name}.")
elif character_choice == "luigi":
    if location_choice == "castle":
        print(f"{name}, brave Luigi sneaks into the castle while Mario distracts the guards!")
    elif location_choice == "forest":
        print(f"{name}, Luigi bounces on mushrooms and uncovers a secret vine to the clouds!")
    elif location_choice == "underground":
        print(f"{name}, Luigi gets lost in the dark but finds a Super Star just in time!")
    else:
        print(f"That place doesn't exist in the Mushroom Kingdom, {name}.")
else:
    print(f"You must choose between Mario or Luigi, {name}.")

# End of adventure
print("\nThanks for playing, " + name + "! Your adventure is just beginning...")
