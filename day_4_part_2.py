import re
import collections

cards = {}
with open("./data/day_4_puzzle.txt") as f:
    puzzle = f.readlines()
    points = []
    for line in puzzle:
        card_number = re.search("(?<=Card).*(?=:)", line)
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
        card_number = card_number.group()
        cards[card_number.strip()] = len(winning_numbers)

scratch_cards = []


def get_cards(card):
    card = int(card)
    copies = cards.get(str(card))
    if copies != 0:
        range_end = copies + 1
        for item in range(1, range_end):
            new_card = card + item
            scratch_cards.append(new_card)
            get_cards(new_card)


for card in cards.keys():
    get_cards(int(card))
    scratch_cards.append(int(card))

print(f"Part 1 answer: {len(scratch_cards)}")
