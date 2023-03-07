key = list(map(int, input().split()))


def find_items(curr_line, symbol):
    start = curr_line.find(symbol)
    end = curr_line.find(symbol, start + 1)
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
    type_treasure = find_items(final_line, "&")

    start_coordinates, end_coordinates = final_line.find("<"), final_line.find(">")
    coordinates = final_line[start_coordinates + 1:end_coordinates]
    print(f"Found {type_treasure} at {coordinates}")