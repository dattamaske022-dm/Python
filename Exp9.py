# Open the file in read mode
file = open("sample.txt", "r")

# Read the contents of the file
content = file.read()

# Print the contents
print("File Contents:")
print(content)

# Close the file
file.close()