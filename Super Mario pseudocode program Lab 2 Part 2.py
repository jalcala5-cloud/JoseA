# Name: Jose 
# Date: 9/02/2025
# Class: CIS188

print("🎮 Welcome to the Endless Mario Adventure! 🎮")

while True:
    name = input("\nEnter your name: ")
    print(f"Hello, {name}! Ready for another adventure?")

    # Choose character
    char = input("Do you want to be Mario or Luigi? ").lower()

    # Choose destination
    place = input("Where do you want to go: castle, forest, or underground? ").lower()

    print("\n--- Your Journey Begins! ---")

    # Adventure decisions
    if char == "mario":
        if place == "castle":
            print(f"{name}, Mario storms Bowser's castle with fiery courage!")
        elif place == "forest":
            print(f"{name}, Mario explores the haunted forest, hopping over Goombas!")
        elif place == "underground":
            print(f"{name}, Mario tunnels underground and unearths hidden coins!")
        else:
            print(f"{name}, Mario isn't sure what '{place}' is—but it's an adventure!")
    elif char == "luigi":
        if place == "castle":
            print(f"{name}, Luigi sneaks into the castle while Mario draws guards’ attention!")
        elif place == "forest":
            print(f"{name}, Luigi bounces on mushrooms in the forest and finds a secret path!")
        elif place == "underground":
            print(f"{name}, Luigi delves underground and discovers a glowing star!")
        else:
            print(f"{name}, Luigi doesn't know where '{place}' is—but he's brave enough to find out!")
    else:
        print(f"{name}, choose Mario or Luigi next time—and the Mushroom Kingdom awaits!")

    # Random power-up loop
    times = random.randint(2, 6)
    print(f"\nPower-ups appear {times} times!")
    for i in range(times):
        print(" Power-Up!")

    # Continue session?
    again = input("\nDoes someone else want to take over? (yes/no) ").lower()
    if again in ("no", "n"):
        print(f"\nThanks for the quest, {name}! The adventure ends here.")
        break