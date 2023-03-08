key = list(map(int, input().split()))


def find_items(curr_line, first_symbol, second_symbol):
    start = curr_line.find(first_symbol)
    end = curr_line.find(second_symbol, start + 1)
    return curr_line[start + 1:end]


while True:
    command = input()
    if command == "find":
        break
    line = list(command)
    for i in range(len(line)):
        num = key[i % len(key)]
        line[i] = chr(ord(line[i]) - num)
    final_line = "".join(line)

    treasure_symbol = "&"
    start_coordinates_symbol = "<"
    end_coordinates_symbol = ">"
    type_treasure = find_items(final_line, treasure_symbol, treasure_symbol)
    coordinates = find_items(final_line, start_coordinates_symbol, end_coordinates_symbol)
    print(f"Found {type_treasure} at {coordinates}")