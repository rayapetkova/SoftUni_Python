text = input().split()

while True:
    line = input()
    if line == "3:1":
        break
    command = line.split()
    first_idx, second_idx = int(command[1]), int(command[2])
    if "merge" in command:
        if first_idx < 0:
            first_idx = 0
        elif second_idx >= len(text):
            second_idx = len(text) - 1
        if first_idx >= second_idx:
            continue
        merged_element = "".join(text[first_idx:second_idx + 1])
        del text[first_idx:second_idx + 1]
        text.insert(first_idx, merged_element)
    elif "divide" in command:
        idx, partitions = int(command[1]), int(command[2])
        parts = len(text[idx]) // partitions
        element = text.pop(idx)
        result = []
        for i in range(partitions - 1):
            result.append(element[:parts])
            element = element[parts:]
        result.append(element)
        for x in result[::-1]:
            text.insert(idx, x)

print(" ".join(text))