numbers = [1, 2, 3, 4, 5]
def square(num):
    return num ** 2

# Use map() with the named function
squared_numbers = list(map(square, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)