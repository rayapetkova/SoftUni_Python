key = list(map(int, input().split()))

while True:
    command = input()
    if command == "find":
        break
    line = list(command)
    for i in range(len(line)):
        num = key[i % len(key)]
        line[i] = chr(ord(line[i]) - num)
    final_line = "".join(line)
    start_type = final_line.find("&")
    end_type = final_line.find("&", start_type + 1)
    type_treasure = final_line[start_type + 1:end_type]

    start_coordinates, end_coordinates = final_line.find("<"), final_line.find(">")
    coordinates = final_line[start_coordinates + 1:end_coordinates]
    print(f"Found {type_treasure} at {coordinates}")