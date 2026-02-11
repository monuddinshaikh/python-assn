# Open a file in write mode
file = open("simple.txt", "w")

# Write text to the file
file.write("Hello, this is a sample text.\n")
file.write("Python makes file handling easy!")

# Close the file
file.close()

print("Text has been written to 'simple.txt'.")
