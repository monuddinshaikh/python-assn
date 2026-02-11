# Sample string
text = "  Hello, Python Programming!  "

print("Original string:", repr(text))

# 1. Convert to uppercase
upper_text = text.upper()
print("Uppercase:", upper_text)

# 2. Convert to lowercase
lower_text = text.lower()
print("Lowercase:", lower_text)

# 3. Remove whitespace from the beginning and end
stripped_text = text.strip()
print("Stripped string:", repr(stripped_text))

# 4. Replace a substring
replaced_text = text.replace("Python", "Java")
print("Replaced string:", replaced_text)

# 5. Split the string into a list of words
words = text.split()
print("Split into words:", words)

# 6. Join a list of words into a string
joined_text = "-".join(words)
print("Joined with '-':", joined_text)

# 7. Check if the string starts with "Hello"
starts_with_hello = text.strip().startswith("Hello")
print("Starts with 'Hello'?", starts_with_hello)

# 8. Check if the string ends with "Programming!"
ends_with_programming = text.strip().endswith("Programming!")
print("Ends with 'Programming!'?", ends_with_programming)

# 9. Find the position of a substring
index_python = text.find("Python")
print("Index of 'Python':", index_python)

# 10. Count occurrences of a character
count_o = text.count("o")
print("Number of 'o' in string:", count_o)
