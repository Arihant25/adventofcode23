import re

# Read the file
with open("2/2.txt", "r") as file:
    lines = file.read().split("\n")

sum = 0

for line in lines:
    game = line.split(":")[1]
    sets = game.split(";")

    colors = [0, 0, 0]  # [blue, red, green]
    for set in sets:
        # Regex to extract the number and color from each set
        finder = re.findall(r"(\d+) (\w+)", set)

        # Find the max count for each color
        for number, color in finder:
            number = int(number)
            if color == "blue":
                colors[0] = max(colors[0], number)
            elif color == "red":
                colors[1] = max(colors[1], number)
            elif color == "green":
                colors[2] = max(colors[2], number)

    power = colors[0] * colors[1] * colors[2]
    sum += power

print(sum)
