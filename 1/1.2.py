# Get input
file = open("1/1.txt", "r")
lines = file.readlines()
file.close()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0


def is_num(num_str):
    for num in numbers:
        if num in num_str:
            return True
    return False


def word_to_num(num_str):
    for num in numbers:
        if num in num_str:
            return str(numbers.index(num) + 1)
    return ""


def get_sum(line):
    num_str = ""
    num_finder = ""

    # Find the first number
    for ch in line:
        if ch.isnumeric():
            num_str = ch
            break
        else:
            num_finder += ch
            if is_num(num_finder):
                num_str = word_to_num(num_finder)
                break

    # Find the last number
    num_finder = ""
    for ch in line[::-1]:
        if ch.isnumeric():
            num_str += ch
            break
        else:
            num_finder = (ch + num_finder).strip()
            if is_num(num_finder):
                num_str += word_to_num(num_finder)
                break

    # Find the sum
    line_sum = int(num_str)
    return line_sum


for line in lines:
    sum += get_sum(line)

print(sum)
