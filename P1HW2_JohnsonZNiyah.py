# ZNiyah Johnson
# 2/16/2025
# P1HW2
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")

budget = int(input("Enter Budget: "))

destination = input("Enter your travel destination: ")

gas_expense = int(input("How much do you think you will spend on gas?: "))

accomodation_expense = int(input("Approximately, how much will you need for accomodation/hotel?: "))

food_expense = int(input("Last, how much do you need for food?: "))


value = gas_expense + accomodation_expense + food_expense


remaining_balance = budget - value

print("\n--------------Travel Expenses---------------")

print("Location: ", destination)
print("Initial Budget: $", budget)

print("Fuel:  $", gas_expense)

print("Accomodation:  $", accomodation_expense)

print("Food:  $", food_expense)

print("Remaining Balance:  $", remaining_balance)


