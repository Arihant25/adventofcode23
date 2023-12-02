import re

# Read the file
with open("2/2.txt", "r") as file:
    lines = file.read().split("\n")

game_number = 0
result = 0

for line in lines:  # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_number += 1
    game_is_valid = False

    game = line.split(":")[1]  # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    sets = game.split(";")

    for set in sets:  # 3 blue, 4 red
        colors = {"blue": 0, "red": 0, "green": 0}

        # Regex to extract the number and color from each set
        finder = re.findall(r"(\d+) (\w+)", set)  # [('3', 'blue'), ('4', 'red')]

        # Add the number of each color to the dictionary
        for number, color in finder:
            colors[color] += int(number)

        # Check if the game is valid
        if colors["blue"] <= 14 and colors["red"] <= 12 and colors["green"] <= 13:
            game_is_valid = True
        else:
            game_is_valid = False
            break

    if game_is_valid:
        result += game_number

print(result)
