# Function to add binary strings
def add_binary(a, b):
    result = bin(int(a, 2) + int(b, 2))
    return result[2:]

# Input
a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

# Output
print("Sum:", add_binary(a, b))