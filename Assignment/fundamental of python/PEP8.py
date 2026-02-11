"""
Simple Calculator Program
----------------------------------------
This program demonstrates:
1. Proper indentation
2. Use of comments
3. Variables following PEP 8 guidelines
"""

# Get input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Perform calculations
addition_result = number1 + number2
subtraction_result = number1 - number2
multiplication_result = number1 * number2

# Handle division with zero check
if number2 != 0:
    division_result = number1 / number2
else:
    division_result = "Error: Cannot divide by zero"

# Display results
print("\nResults:")
print("Addition:", addition_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)
