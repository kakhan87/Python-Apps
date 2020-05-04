# Task 1

# Input base length in cm

base_length = float(input("What is the base length of the triangle (in cm)? "))

while (base_length <=0) :
    print("**Error - the base length must be a positive number. You entered",     
          int(base_length))
    base_length = float(input("What is the base length of the triangle (in cm)? "))


# Input height in cm
height = float(input("What is the height of the triangle (in cm)? "))

while (height <=0) :
    print("**Error - the height must be a positive number. You entered",
          int(height))
    height = float(input("What is the height of the triangle (in cm)? "))
          
# Calculate area of triangle in sq m
area_triangle = 0.5 * (base_length) * (height)

# Print result
print("A triangle with a base of ", base_length, " cm and height of ", height,
      " cm has an area of ", int(area_triangle), " sq cm", sep="")
