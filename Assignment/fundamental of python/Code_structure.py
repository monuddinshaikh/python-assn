# 1. Comment: This is a Student Result Program

# 2. Variables
student_name = "Ravi"
marks = 72

# 3. Output
print("Student Name:", student_name)
print("Marks:", marks)

# 4. Conditional Statement
if marks >= 40:
    print("Result: Pass ✅")
else:
    print("Result: Fail ❌")

# 5. Loop: Printing marks for 3 subjects
subjects = [85, 72, 90]
print("\nMarks in subjects:")
for score in subjects:
    print(score)

# 6. Function: Calculate Average
def calculate_average(scores):
    return sum(scores) / len(scores)

average = calculate_average(subjects)
print("\nAverage Marks:", average)
