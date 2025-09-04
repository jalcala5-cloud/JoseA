#Lab 1
#Name: Jose Serafin Alcala Moreno
#Date: 8/26/2025
#Class: CIS188

# Ask for the user's name
name = input("What is your name?\n")

# Greet the user
print("Hello,", name)

# Ask for the user's age
age = int(input("What is your age?\n"))

# Calculate the number of letters in the name
name_length = len(name)

# Add the number of letters in the name to the age
new_number = age + name_length

# Print the final message
print(f"{name}, if we add the number of letters in your name to your")
print(f"age then you will be {new_number} in {name_length} years.")