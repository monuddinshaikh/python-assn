from functools import reduce
numbers = [1, 2, 3, 4, 5]

def multiply(x, y):
    return x * y

# Use reduce() to compute the product of the list
product = reduce(multiply, numbers)

print("Numbers:", numbers)
print("Product of all numbers:", product)