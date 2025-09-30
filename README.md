# Function to perform addition and subtraction
def add_subtract(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
sum_result, diff_result = add_subtract(num1, num2)

# Display results
print(f"Addition: {num1} + {num2} = {sum_result}")
print(f"Subtraction: {num1} - {num2} = {diff_result}")
