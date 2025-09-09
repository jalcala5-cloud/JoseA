# Name: Jose Alcala
# Date: 10/10/2023
# Class: CIS 188

# Description: A program to track student grades with functionalities to add, update, remove, display

def main():
    grades = {}

    while True:
        action = input("Choose an action: add, update, remove, display, get, exit\n").strip().lower()

        if action == "add":
            name = input("Enter student name: ").strip()
            if name in grades:
                print(f"{name} is already in the list with grade {grades[name]}.")
            else:
                try:
                    grade = int(input("Enter grade (0-100): "))
                    grades[name] = grade
                    print(f"{name} added with grade {grade}.")
                except ValueError:
                    print("Invalid grade. Please enter a number.")
                    
        elif action == "update":
            name = input("Enter student name to update: ").strip()
            if name in grades:
                try:
                    grade = int(input(f"Enter new grade for {name}: "))
                    grades[name] = grade
                    print(f"{name}'s grade updated to {grade}.")
                except ValueError:
                    print("Invalid grade. Please enter a number.")
            else:
                print(f"{name} is not in the list.")
                
        elif action == "remove":
            name = input("Enter student name to remove: ").strip()
            if name in grades:
                del grades[name]
                print(f"{name} has been removed.")
            else:
                print(f"{name} is not in the list.")
                
        elif action == "display":
            if grades:
                print("Student Grades:")
                for student, grade in grades.items():
                    print(f"{student}: {grade}")
            else:
                print("No students in the list.")
                
        elif action == "get":
            name = input("Enter student name: ").strip()
            grade = grades.get(name)
            if grade is not None:
                print(f"{name}'s grade is {grade}.")
            else:
                print(f"{name} is not in the list.")
                
        elif action == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown action. Please try again.")

if __name__ == "__main__":
    main()
