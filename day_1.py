import csv

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
print(answer)
