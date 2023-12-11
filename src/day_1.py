import csv
import re

# Part 1.
numbers = []
with open("./data/day_1_puzzle.txt") as f:
    reader = csv.reader(f)
    for line in reader:
        digits = []
        for character in line[0]:
            try:
                digit = int(character)
                digits.append(digit)
            except ValueError:
                pass
        numbers.append(digits)

    correct_numbers = []
    for row_digits in numbers:
        if len(row_digits) > 1:
            number = str(row_digits[0]) + str(row_digits[-1])
            correct_numbers.append(int(number))
        else:
            number = str(row_digits[0]) + str(row_digits[0])
            correct_numbers.append(int(number))

answer = sum(correct_numbers)
print(f"Part 1 answer: {answer}")

# Part 2.
WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

numbers = []
with open("./data/day_1_puzzle.txt") as f:
    reader = csv.reader(f)
    for line in reader:
        digits = {}
        for word in WORDS.keys():
            matches = re.finditer(word, line[0])
            for match in matches:
                digits[match.start()] = WORDS.get(match.group())
        for position, character in enumerate(line[0]):
            try:
                digit = int(character)
                digits[position] = digit
            except ValueError:
                pass

        if len(digits) != 0:
            numbers.append(digits)


correct_numbers = []
for row_digits in numbers:
    row_digits = dict(sorted(row_digits.items()))
    row_digits = list(row_digits.values())
    if len(row_digits) > 1:
        number = str(row_digits[0]) + str(row_digits[-1])
        correct_numbers.append(int(number))
    else:
        number = str(row_digits[0]) + str(row_digits[0])
        correct_numbers.append(int(number))

answer = sum(correct_numbers)
print(f"Part 2 answer: {answer}")
