# string print!
def string_print(text):
    print(text)

string_print("Hello, welcome to pyhton programming...")

# Create a calculator using function!

def add(a, b):
    return a + b 

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
    
menu = """
Simmple calculator.
1. Addition
2. Substraction
3. Multiplication
4. Division 
"""

print(menu)

choice = int(input("Enter choice for menu (1 - 4): "))
if choice == (1 - 5):
    num1 = int(input("Enter First number: "))
    num2 = int(input("Enter Second number: "))

if choice == 1:
    print("Result: ", add(num1, num2)) 

elif choice == 2:
    print("Result: ", sub(num1, num2))

elif choice == 3:
    print("Result: ", mul(num1, num2))

elif choice == 4:
    print("Result: ", div(num1, num2))

else:
    print("Invalid choice!")