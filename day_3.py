import re

with open("./data/day_3_puzzle.txt") as f:
    puzzle = f.readlines()

LINE_LENGTH = 140  # Important.

# Part 1.

# Find position of numbers.
numbers = []
for line_number, line in enumerate(puzzle):
    matches = re.finditer("[0-9][0-9][0-9]|[0-9][0-9]|[0-9]", line)
    for match in matches:
        try:
            number_dictionary = {}
            number = match.group()
            start = match.start()
            end = match.end()
            end = end - 1
            middle = end - 1
            multiplier = line_number * LINE_LENGTH
            start = start + multiplier
            middle = middle + multiplier
            end = end + multiplier
            number_dictionary[number] = [start, middle, end]
            numbers.append(number_dictionary)
        except AttributeError:
            pass

# Find position of symbols.
symbols = []
for line_number, line in enumerate(puzzle):
    matches = re.finditer("\*|\#|\+|\$|\&|\/|%|@|=|\-", line)
    for match in matches:
        try:
            multiplier = line_number * LINE_LENGTH
            position = match.start()
            position = position + multiplier
            symbols.append(position)
        except AttributeError:
            pass

part_numbers = []
# Check to see which numbers are adjacent to symbols.
for item in numbers:
    for number, positions in item.items():
        for position in positions:
            number_left = position - 1
            number_right = position + 1
            number_behind = position - LINE_LENGTH
            number_ahead = position + LINE_LENGTH
            number_behind_left = number_behind - 1
            number_behind_right = number_behind + 1
            number_ahead_left = number_ahead - 1
            number_ahead_right = number_ahead + 1
            if (
                number_behind in symbols
                or number_left in symbols
                or number_right in symbols
                or number_ahead in symbols
                or number_ahead_left in symbols
                or number_ahead_right in symbols
                or number_behind_left in symbols
                or number_behind_right in symbols
            ):
                part_numbers.append(int(number))
                break

answer = sum(part_numbers)
print(answer)
