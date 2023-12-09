import re

# Parsing puzzle.
my_numbers = []
winning_numbers = []
with open("./data/day_4_puzzle.txt") as f:
    puzzle = f.readlines()
    for line in puzzle:
        line_my_numbers = re.search("(?<=\|).*", line)
        line_my_numbers = line_my_numbers.group().split()
        my_numbers.append(line_my_numbers)
        line_winning_numbers = re.search("(?<=:).*(?=\|)", line)
        line_winning_numbers = line_winning_numbers.group().split()
        winning_numbers.append(line_winning_numbers)

# Identifying winning numbers.
matches = []
for game_number in range(0, 220):
    matched_numbers = []
    for my_number in my_numbers[game_number]:
        if my_number in winning_numbers[game_number]:
            matched_numbers.append(int(my_number))
    matches.append(matched_numbers)

# Calculating the puzzle answer.
points = []
for game_number, game in enumerate(matches):
    length = len(matches[game_number]) - 1
    for index, number in enumerate(matches[game_number]):
        if index == 0:
            point = 1
        else:
            point = point * 2
        if int(index) == length:
            points.append(point)

answer = sum(points)
print(answer)
