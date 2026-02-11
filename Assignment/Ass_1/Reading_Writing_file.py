# Ask the user for the filename
filename = input("Enter the filename to read: ")

with open(filename, 'r') as file:
    contents = file.read()
    print("\nFile Contents:\n")
    print(contents)

# Multiple string into file.
filename = input("Enter the filename to write into: ")

num_lines = int(input("How many lines do you want to write? "))

with open(filename, 'w') as file:
    for i in range(num_lines):
        line = input(f"Enter line {i+1}: ")
        file.write(line + '\n')  # Write the line and add a newline character

print(f"{num_lines} lines have been written to '{filename}'.")