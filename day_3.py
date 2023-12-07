import re

with open("./data/day_3_example.txt") as f:
    puzzle = f.readlines()

for line_number, line in enumerate(puzzle):
    pattern = re.search("[0-9][0-9][0-9]|[0-9][0-9]|[0-9]", line)
    try:
        print(pattern.group())
        print(pattern.start())
    except AttributeError:
        pass
