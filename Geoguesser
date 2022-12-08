from PIL import Image
import random

# Define a list of locations and their corresponding images
locations = [
  {"name": "Paris", "image": "paris.jpg"},
  {"name": "New York", "image": "new_york.jpg"},
  {"name": "Tokyo", "image": "tokyo.jpg"},
  {"name": "Sydney", "image": "sydney.jpg"},
  {"name": "Rio de Janeiro", "image": "rio.jpg"},
]

# Select a random location from the list
location = random.choice(locations)

# Open the image file for the location
image = Image.open(location["image"])

# Display the image
image.show()

# Ask the player to guess the location
guess = input("Where is this? ")

# Check if the player's guess is correct
if guess.lower() == location["name"].lower():
  print("Correct!")
else:
  print("Incorrect. The correct answer is:", location["name"])
To play the game, you will need to have the Pillow library installed and have some images of different locations saved in the same directory as the Python script. When you run the script, it will select a random location from the list and display the corresponding image. The player can then enter their guess and the game will check if it is correct.

This is just a simple example of how you can create a game with pictures to guess the location. You can modify the code to add more locations, include different image formats, or add additional features to make the game more challenging and fun.
