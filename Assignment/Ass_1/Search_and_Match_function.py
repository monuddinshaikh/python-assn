import re

# Use re.search() function...
# Input string
text = "Python is a powerful programming language."

# Word to search
word_to_search = "powerful"

# Use re.search() to find the word
match = re.search(rf"\b{word_to_search}\b", text)

if match:
    print(f"The word '{word_to_search}' was found in the string.")
else:
    print(f"The word '{word_to_search}' was NOT found in the string.")

# Use re.match() function...
word_to_match = "Python"

# use re.match() to ckeck for a match at the begining.
match1 = re.match(rf"\b{word_to_match}\b", text)

if match:
    print(f"The word '{word_to_match}' was found in the string.")

else:
    print(f"This word '{word_to_match}' was NOT found in the string.")
