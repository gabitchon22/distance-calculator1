import math

# Get the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Get the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the squared differences between the coordinates
x_difference = math.pow(x2 - x1, 2)
y_difference = math.pow(y2 - y1, 2)

# Calculate the distance using the Euclidean distance formula
distance = math.sqrt(x_difference + y_difference)

# Display the distance rounded to two decimal places
print(f"\nThe distance between the two points is: {distance:.2f}")

# Reflection:
# Using a math library is more practical because it provides ready-made
# functions that simplify calculations and reduce coding errors.
# In this program, sqrt() calculates the square root, while pow() raises
# numbers to a power, making the distance formula easier to implement.
