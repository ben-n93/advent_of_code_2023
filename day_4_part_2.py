import re

"""
# Parsing puzzle.
games = {}
my_numbers = []
winning_numbers = []
with open("./data/day_4_example.txt") as f:
    puzzle = f.readlines()
    for line in puzzle:
        game_number = re.search("(?<=Card).*(?=:)", line)
        line_my_numbers = re.search("(?<=\|).*", line)
        line_my_numbers = line_my_numbers.group().split()
        my_numbers.append(line_my_numbers)
        line_winning_numbers = re.search("(?<=:).*(?=\|)", line)
        line_winning_numbers = line_winning_numbers.group().split()
        winning_numbers.append(line_winning_numbers)
        games[game_number.group()] = {
            "my_numbers": my_numbers,
            "winning_numbers": winning_numbers,
        }
"""

# Parsing puzzle.
my_numbers = []
winning_numbers = []
with open("./data/day_4_example.txt") as f:
    puzzle = f.readlines()
    for line in puzzle:
        line_my_numbers = re.search("(?<=\|).*", line)
        line_my_numbers = line_my_numbers.group().split()
        my_numbers.append(line_my_numbers)
        line_winning_numbers = re.search("(?<=:).*(?=\|)", line)
        line_winning_numbers = line_winning_numbers.group().split()
        winning_numbers.append(line_winning_numbers)

# Identifying winning numbers.
matches = {}
for game_number in range(0, 6):
    matched_numbers = []
    for my_number in my_numbers[game_number]:
        if my_number in winning_numbers[game_number]:
            matched_numbers.append(int(my_number))
    actual_game_number = game_number + 1
    copies = len(matched_numbers)
    matches[actual_game_number] = {
        "copies": copies
        # ,"original_numbers": matched_numbers,
    }

print(matches)
