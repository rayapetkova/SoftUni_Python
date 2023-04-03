def collect(second, items):
    if second not in items:
        items.append(second)


def drop(second, items):
    if second in items:
        items.remove(second)


def combine(second, items):
    second_split = second.split(":")
    old_item = second_split[0]
    new_item = second_split[1]
    if old_item in items:
        idx_old_item = items.index(old_item)
        items.insert(idx_old_item + 1, new_item)


def renew(second, items):
    if second in items:
        items.remove(second)
        items.append(second)


current_items = input().split(", ")

while True:
    line = input()
    if line == "Craft!":
        print(", ".join(current_items))
        break
    command = line.split(" - ")
    current_first = command[0]
    current_second = command[1]

    if current_first == "Collect":
        collect(current_second, current_items)
    elif current_first == "Drop":
        drop(current_second, current_items)
    elif current_first == "Combine Items":
        combine(current_second, current_items)
    elif current_first == "Renew":
        renew(current_second, current_items)