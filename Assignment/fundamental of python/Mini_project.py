# ==============================
# Grade Management System
# ==============================

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# Function to display menu
def menu():
    print("\n===== Grade Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

# Main Program
students = {}  # Dictionary: {name: percentage}

while True:
    menu()
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks (out of 100): "))
        grade = calculate_grade(marks)
        students[name] = (marks, grade)
        print(f"{name}'s data saved successfully!")

    elif choice == 2:
        if not students:
            print("No student records available.")
        else:
            print("\n--- Student Records ---")
            for name, (marks, grade) in students.items():
                print(f"Name: {name}, Marks: {marks}, Grade: {grade}")

    elif choice == 3:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
