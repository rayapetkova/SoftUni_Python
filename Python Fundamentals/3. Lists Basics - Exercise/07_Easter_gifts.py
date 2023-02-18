gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        while "None" in gifts:
            gifts.remove("None")
        print(' '.join(gifts))
        break
    if "OutOfStock" in command:
        command = command.split()
        product = command[1]
        while product in gifts:
            gifts = ["None" if item == product else item for item in gifts]
    elif "Required" in command:
        command = command.split()
        new_gift = command[1]
        index_new_gift = int(command[2])
        if (index_new_gift < len(gifts) - 1) and (index_new_gift >= 0):
            gifts[index_new_gift] = new_gift
    elif "JustInCase" in command:
        command = command.split()
        the_new_gift = command[1]
        gifts[-1] = the_new_gift