# Sample string
text = "Hello, Python!"

first_char = text[0]  # H
print("First character:", first_char)

slice1 = text[2:5]  # llo
print("Slice from index 2 to 5:", slice1)

slice2 = text[:5]  # Hello
print("Slice from start to index 5:", slice2)

slice3 = text[7:]  # Python!
print("Slice from index 7 to end:", slice3)

slice4 = text[:]  # Hello, Python!
print("Complete string using slicing:", slice4)

slice5 = text[::2]  # Hlo yhn
print("Every 2nd character:", slice5)

reversed_text = text[::-1]  # !nohtyP ,olleH
print("Reversed string:", reversed_text)
