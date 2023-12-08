import re

with open("./data/day_3_puzzle.txt") as f:
    puzzle = f.readlines()

numbers = []
for line in puzzle:
    print(len(line))
