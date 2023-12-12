import re

# import pandas as pd


def map_sources(map_row):
    mapped = {}
    category = int(map_row[0])
    seed = int(map_row[1])
    range_end = int(map_row[2])
    for number in range(0, range_end):
        if number == 0:
            mapped[seed] = category
        else:
            new_seed = seed + number
            new_category = category + number
            mapped[new_seed] = new_category
    return mapped


with open("./data/day_5_example.txt", "r") as f:
    lines = f.readlines()
    maps = []
    map_row_dictionaries = []
    total_lines = len(lines)
    # seed-to-soil, soil-to-fertilizer, etc.
    for index, line in enumerate(lines):
        if len(line) != 1:
            line = line.strip()
            # Seeds.
            try:
                seeds = re.search("(?<=seeds:).*", line).group().split()
                continue
            except AttributeError:
                pass
            # Check to see if new map.
            if index + 1 == total_lines:
                maps.append(map_row_dictionaries)
            if re.search("^[a-z].*", line) is not None:
                maps.append(map_row_dictionaries)
                map_row_dictionaries = []
            else:
                try:
                    line = line.strip()
                    numbers = re.search("[0-9].*", line).group()
                    numbers = str(numbers).split()
                    map_row_dictionaries.append(map_sources(numbers))

                except:
                    pass

    final_seeds = {}
    for item in seeds:
        final_seeds[int(item)] = []

    maps = filter(None, maps)
    for almanc_map in maps:
        # Joining each map's rows into a final dictionary.
        final_dictionary = {}
        for dictionary in almanc_map:
            final_dictionary = final_dictionary | dictionary
        # print(final_dictionary)
        # Finding category map location for each seed.
        # print(final_dictionary)
        for seed in seeds:
            # print(seed)
            seed = int(seed)
            category = final_dictionary.get(seed)
            # print(category)
            if category is not None:
                final_seeds[seed].append(category)
            else:
                final_seeds[seed].append(seed)

    print(final_seeds)
