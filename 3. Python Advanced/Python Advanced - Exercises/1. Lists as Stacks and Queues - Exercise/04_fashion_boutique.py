clothes_box_stack = list(map(int, input().split()))
one_rack_capacity = int(input())
sum_elements = 0
racks = 0

while clothes_box_stack:
    element = clothes_box_stack.pop()
    sum_elements += element

    if sum_elements == one_rack_capacity:
        racks += 1
        sum_elements = 0

    elif sum_elements > one_rack_capacity:
        clothes_box_stack.append(element)
        racks += 1
        sum_elements = 0

    if not clothes_box_stack and sum_elements > 0:
        racks += 1

print(racks)
