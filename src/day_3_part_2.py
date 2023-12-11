import re

with open("./data/day_3_puzzle.txt") as f:
    puzzle = f.readlines()

LINE_LENGTH = 140  # Important.

# Find position of numbers.
numbers = {}
for line_number, line in enumerate(puzzle):
    matches = re.finditer("[0-9][0-9][0-9]|[0-9][0-9]|[0-9]", line)
    for match in matches:
        try:
            number = match.group()
            start = match.start()
            end = match.end()
            end = end - 1
            middle = end - 1
            multiplier = line_number * LINE_LENGTH
            start = start + multiplier
            middle = middle + multiplier
            end = end + multiplier
            numbers[start] = number
            numbers[middle] = number
            numbers[end] = number
        except AttributeError:
            pass

# Find position of symbols.
symbols = []
for line_number, line in enumerate(puzzle):
    matches = re.finditer("\*", line)
    for match in matches:
        try:
            multiplier = line_number * LINE_LENGTH
            position = match.start()
            position = position + multiplier
            symbols.append(position)
        except AttributeError:
            pass

new_symbols = {}

# Check to see which numbers are adjacent to symbols.
for symbol in symbols:
    surrounding_positions = []
    number_left = symbol - 1
    number_right = symbol + 1
    number_behind = symbol - LINE_LENGTH
    number_ahead = symbol + LINE_LENGTH
    number_behind_left = number_behind - 1
    number_behind_right = number_behind + 1
    number_ahead_left = number_ahead - 1
    number_ahead_right = number_ahead + 1
    surrounding_positions.append(number_left)
    surrounding_positions.append(number_right)
    surrounding_positions.append(number_behind)
    surrounding_positions.append(number_ahead)
    surrounding_positions.append(number_behind_left)
    surrounding_positions.append(number_behind_right)
    surrounding_positions.append(number_ahead_left)
    surrounding_positions.append(number_ahead_right)
    new_symbols[symbol] = surrounding_positions

parts = {}
for number, positions in new_symbols.items():
    matching_numbers = []
    for position in positions:
        matched_number = numbers.get(position)
        if matched_number is not None:
            matching_numbers.append(matched_number)
    unique_values = set(matching_numbers)
    parts[number] = list(unique_values)

valid_parts = []
for gear, parts in parts.items():
    if len(parts) == 2:
        gear_ratio = int(parts[0]) * int(parts[1])
        valid_parts.append(gear_ratio)

answer = sum(valid_parts)
print(answer)
