import re

WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

text = "2twotdjdfbqtqxrs1192"
test = "888"

matches = re.finditer(test, text)
bar = {}
for match in matches:
    bar[1] = match.start()

print(bar)
