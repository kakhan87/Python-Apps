# Task 3

number_of_eggs = float(input("Enter number of eggs: "))

if (number_of_eggs >= 0 and number_of_eggs < 4 * 12):
    price_per_dozen = 0.5

elif (number_of_eggs >= 4 * 12 and number_of_eggs < 6 * 12):
    price_per_dozen = 0.45

elif (number_of_eggs >= 6 * 12 and number_of_eggs < 11 * 12):
    price_per_dozen = 0.4   

elif (number_of_eggs >= 11 * 12):
    price_per_dozen = 0.35
    
else:
    print("Invalid value. Value must be greater than zero.")
    

print("Your cost is $", price_per_dozen," or ", round(price_per_dozen / 12, 3), " per egg.", sep = "")
print("Your bill comes to $", round(number_of_eggs / 12 * price_per_dozen, 3), sep = "")
