# ZNiyah Johnson

# Date: 4-3-25

# Assignment: P4HW1

# A brief description of the project:
# This program asks the user how many scores they want to input, 
# validates the scores to ensure they are between 0 and 100, 
# and then calculates and displays the lowest score, the modified list of scores, 
# the average of the remaining scores, and the letter grade based on the average score.

# Pseudocode:
# 1. Ask the user how many scores they want to input.
# 2. Initialize an empty list for scores.
# 3. Collect scores in a loop, validate them, and add valid scores to the list.
# 4. Calculate the lowest score, remove it from the list, and compute the average of the remaining scores.
# 5. Determine the letter grade based on the average.
# 6. Display the results.

# Step 1: Ask how many scores to enter
num_scores = int(input("How many scores would you like to enter? "))

# Step 2: Initialize an empty list to store the scores
scores = []

# Step 3: Collect and validate the scores
i = 0  # Counter for how many scores we've entered
while i < num_scores:
    score = float(input(f"Enter score #{i + 1}: "))
    
    if 0 <= score <= 100:  # Check if the score is valid
        scores.append(score)
        i += 1  # Increase the counter only if the score is valid
    else:
        print("Invalid score! Please enter a score between 0 and 100.")

# Step 4: Find the lowest score and remove it
lowest_score = min(scores)
scores.remove(lowest_score)

# Step 5: Calculate the average of the remaining scores
average_score = sum(scores) / len(scores)

# Step 6: Determine the letter grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

# Step 7: Display the results
print(f"Lowest score entered: {lowest_score}")
print(f"Modified List: {scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade: {grade}")
