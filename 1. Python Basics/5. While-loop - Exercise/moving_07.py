width = int(input())
length = int(input())
height = int(input())

space = width * length * height

boxes_space = 0

while True:
    boxes_num = input()
    if boxes_num != "Done":
        boxes_num = int(boxes_num)
        boxes_space = boxes_space + boxes_num
        if boxes_space >= space:
            print(f"No more free space! You need {boxes_space - space} Cubic meters more.")
            break

    if boxes_num == "Done":
        if boxes_space >= space:
            print(f"No more free space! You need {boxes_space - space} Cubic meters more.")
        else:
            print(f"{space - boxes_space} Cubic meters left.")
        break