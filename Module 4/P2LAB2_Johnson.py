# ZNiyah Johnson
# 2-25-25
# P2LAB2
# Write a program that creates a dictionary

# create dictionary

cars = {"Camaro": 18.21,
     "Prius": 52.36,
     "Model S": 110, 
      "Silverado": 26}

# display results of all keys in dictionary
keys = cars.keys()
print(keys)
print()

car_input = input("Enter a vehicle to see it's mpg: ")
print()
mpg_output = cars[car_input]

# Display output
print(f'The {car_input} gets {mpg_output} mpg.\n')
