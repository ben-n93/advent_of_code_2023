import re

# Parsing puzzle.
my_numbers = []
winning_numbers = []
with open("./data/day_4_puzzle.txt") as f:
    puzzle = f.readlines()
    points = []
    for line in puzzle:
        line_winning_numbers = re.search("(?<=:).*(?=\|)", line)
        line_winning_numbers = set(line_winning_numbers.group().split())
        line_my_numbers = re.search("(?<=\|).*", line)
        line_my_numbers = set(line_my_numbers.group().split())
        winning_numbers = line_winning_numbers.intersection(line_my_numbers)
        if winning_numbers:
            for index, number in enumerate(winning_numbers):
                if index == 0:
                    point = 1
                else:
                    point = point * 2
            points.append(point)
    answer = sum(points)
    print(answer)
