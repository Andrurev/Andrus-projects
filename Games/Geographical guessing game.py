import random

# Define a list of geographical locations and their corresponding countries
locations = [
    ("Mount Everest", "Nepal"),
    ("Sydney Opera House", "Australia"),
    ("Taj Mahal", "India"),
    ("Great Barrier Reef", "Australia"),
    ("Machu Picchu", "Peru"),
    ("Pyramids of Giza", "Egypt"),
    ("Eiffel Tower", "France"),
    ("Grand Canyon", "United States"),
    ("London Eye", "United Kingdom"),
    ("Statue of Liberty", "United States"),
]

# Shuffle the list of locations randomly
random.shuffle(locations)

# Keep track of the number of correct answers
correct_answers = 0

# Loop through the locations and ask the user to guess the country
for location, country in locations:
    # Print the location
    print(location)

    # Get the user's guess for the country
    guess = input("Enter the name of the country: ")

    # Check if the guess is correct
    if guess.lower() == country.lower():
        print("Correct!\n")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is {country}.\n")

# Print the final score
total_questions = len(locations)
score = correct_answers / total_questions * 100
print(f"You scored {score:.2f}% ({correct_answers} out of {total_questions}).")
