# Take input from user
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True  # assume number is prime
    for i in range(2, num):
        if num % i == 0:   # if divisible by any number
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
