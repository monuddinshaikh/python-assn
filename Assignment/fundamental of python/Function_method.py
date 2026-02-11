# using string
print("Hello")

# Allocate the string.
message = "HELLO, PYTHON"

print(message)

# Using triple quotes to store a multi-line string
message = """Hello, Python!
Welcome to learning strings.
Triple quotes allow multiple lines."""

print(message)

# Accessing the first character using index 0
text = "Python"
first_char = text[0]

print("The first character is:", first_char)

# using the slicing.
substring = text[1:]
print("String from the second position onwards:", substring)

# Access the fifth character.
substring = text[:5]
print("String up to the fifth character:", substring)

# Substring using.
substring = text[1:4]
print("Substring between index 1 and 4:", substring)

# Access the last character.
last_char = text[-1]
print("The last character is:", last_char)

# Access the alternate character.
alternate_chars = text[1::2]
print("Every alternate character from index 1:", alternate_chars)
