print("This program calculates and displays travel expenses\n")

# Request information

budget = float(input("Enter Budget: "))
print()

location = input("Enter your travel destination: ")

print()
fuel = float(input("How much do you think you will spend on gas? "))

print()

hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))

# add expenses

expenses = fuel + hotel+ food

remainAmount = budget - expenses

# display results

print("\n------------Travel Expenses------------")

print(f"{"Location: ":<20} {location}")
print(f"{"Budget: ":<20} ${budget:.2f}")
print(f"{"Fuel: ":<20} ${fuel:.2f}")
print(f"{"Accomodation: ":<20} ${hotel:.2f}")
print(f"{"Food: ":<20} ${food:.2f}")
print("--------------------------------------\n")
print(f"{"Remaining Balance: ":<20} ${remainAmount:.2f}")




