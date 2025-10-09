# Name:Jose Alcala
# Date:10/09/2025
# A small text-based adventure game.
#Tiny Adventure Game

def go_direction(room, direction):
    if direction in room["exits"]:
        return room["exits"][direction]
    return ""

rooms = {
    "cave": {
        "desc": "You are in a small cave. Passages lead north and east.",
        "exits": {"north": "forest", "east": "lake"},
        "items": ["torch"]
    },
    "forest": {
        "desc": "You are in a dark forest. You hear wolves howling.",
        "exits": {"south": "cave", "up": "mountain"},
        "items": ["stick"]
    },
    "lake": {
        "desc": "You stand by a serene lake. The water is crystal clear.",
        "exits": {"west": "cave"},
        "items": ["fish"]
    },
    "mountain": {
        "desc": "You climb to a snowy mountain peak. The wind howls around you.",
        "exits": {"down": "forest"},
        "items": ["rock"]
    }
}

def show_room(room):
    print("\n" + room["desc"])
    if room.get("items"):
        print("You see:", ", ".join(room["items"]))
    print("Exits:", ", ".join(room["exits"].keys()))

inventory = []

def take_item(item, room):
    if item in room.get("items", []):
        room["items"].remove(item)
        inventory.append(item)
        print(f"You take the {item}.")
    else:
        print(f"There is no {item} here.")

def show_inventory():
    if inventory:
        print("You have:", ", ".join(inventory))
    else:
        print("You are carrying nothing.")

current_room = "cave"
print("Welcome to Tiny Adventure!")
show_room(rooms[current_room])

while True:
    command = input("\n→ ").strip().lower().split()

    if not command:
        continue
    if command[0] in ["quit", "exit"]:
        print("Goodbye, adventurer!")
        break
    elif command[0] == "go" and len(command) > 1:
        next_room = go_direction(rooms[current_room], command[1])
        if next_room:
            current_room = next_room
            show_room(rooms[current_room])
        else:
            print("You can’t go that way.")
    elif command[0] == "take" and len(command) > 1:
        take_item(command[1], rooms[current_room])
    elif command[0] == "inventory":
        show_inventory()
    elif command[0] == "look":
        show_room(rooms[current_room])
    else:
        print("I don’t understand that command.")
