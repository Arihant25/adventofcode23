# Get input
file = open("1.txt", "r")
lines = file.readlines()
file.close()

sum = 0

for line in lines:
    num_str = ""

    # Find the first number
    for ch in line:
        if ch.isnumeric():
            num_str = ch
            break

    # Find the last number
    for ch in line[::-1]:
        if ch.isnumeric():
            num_str += ch
            break

    # Find the sum
    sum += int(num_str)

print(sum)
