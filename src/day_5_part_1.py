import re


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


def join_map_rows(almanc_map, seeds):
    if almanc_map is not None:
        # Final seeds dictionary.
        final_seeds = {}
        for item in seeds:
            final_seeds[int(item)] = []
        # Joining each map's rows into a final dictionary.
        final_dictionary = {}
        for dictionary in almanc_map:
            final_dictionary = final_dictionary | dictionary
        # Finding category map location for each seed.
        for seed in seeds:
            seed = int(seed)
            category = final_dictionary.get(seed)
            if category is not None:
                final_seeds[seed] = category
            else:
                final_seeds[seed] = seed
        final_seeds = [value for value in final_seeds.values()]
        return final_seeds
    return seeds


with open("./data/day_5_puzzle.txt", "r") as f:
    lines = f.readlines()
    map_row_dictionaries = []
    total_lines = len(lines)
    for index, line in enumerate(lines):
        print(index)
        line = line.strip()
        # Seeds.
        if re.search("(?<=seeds:).*", line):
            seeds = re.search("(?<=seeds:).*", line).group().split()
        else:
            if index + 1 == total_lines:
                numbers = re.search("[0-9].*", line).group()
                numbers = str(numbers).split()
                map_row_dictionaries.append(map_sources(numbers))
                seeds = join_map_rows(map_row_dictionaries, seeds)
                print(seeds)  # Part 1 answer.
            if re.search("^[a-z].*", line) is not None:
                # print(index, line)
                seeds = join_map_rows(map_row_dictionaries, seeds)
                map_row_dictionaries = []
                # print(seeds)
            else:
                try:
                    numbers = re.search("[0-9].*", line).group()
                    numbers = str(numbers).split()
                    map_row_dictionaries.append(map_sources(numbers))
                except:
                    pass

    # maps = filter(None, maps)
