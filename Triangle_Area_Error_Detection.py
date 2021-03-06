# Task 1

import sys

# Input base length in cm
base_length = float(input("What is the base length of the triangle (in cm)? "))
if not (base_length > 0):
    print("**Error - the base length must be a positive number. You entered",
          int(base_length))
    sys.exit()

# Input height in cm
height = float(input("What is the height of the triangle (in cm)? "))
if not (height > 0):
    print("**Error - the height must be a positive number. You entered",
          int(height))
    sys.exit()
          
# Calculate area of triangle in sq m
area_triangle = 0.5 * (base_length) * (height)

# Print result
print("A triangle with a base of ", base_length, " cm and height of ", height,
      " cm has an area of ", int(area_triangle), " sq cm", sep="")
