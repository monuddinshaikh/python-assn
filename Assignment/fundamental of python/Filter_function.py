numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_odd(num):
    return num % 2 != 0

# Using filter() to get only odd numbers
odd_numbers = list(filter(is_odd, numbers))

print("Odd numbers:", odd_numbers)
