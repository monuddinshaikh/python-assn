# Exception handeling in simple calculator.
def simple_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Select operation: +, -, *, /")
        operation = input("Enter operation: ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2  
        else:
            print("Invalid operation selected.")
            return
        
        print(f"The result of {num1} {operation} {num2} is: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

simple_calculator()

# Demonstrate multiple error handelling...
def multiple_exceptions_demo():
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        result = num1 / num2  
        print(f"Result of {num1} / {num2} is {result}")

        my_list = [1, 2, 3]
        index = int(input("Enter an index to access in the list (0-2): "))
        print(f"Element at index {index} is {my_list[index]}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except ValueError:
        print("Error: Invalid input! Please enter integers only.")

    except IndexError:
        print("Error: Index out of range! Please enter 0, 1, or 2.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

multiple_exceptions_demo()
