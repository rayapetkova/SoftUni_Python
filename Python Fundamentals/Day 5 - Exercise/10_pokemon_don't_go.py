def increase_and_decrease(element, numbers, index):
    if 0 <= index < len(numbers):
        numbers.pop(index)
    for i in range(len(numbers)):
        if numbers[i] <= element:
            numbers[i] += element
        else:
            numbers[i] -= element


current_numbers = [int(j) for j in input().split()]
removed_elements = 0

while True:
    if len(current_numbers) <= 0:
        break
    idx = int(input())
    if 0 <= idx < len(current_numbers):
        removed_elements += current_numbers[idx]
        current_element = int(current_numbers[idx])
        increase_and_decrease(current_element, current_numbers, idx)

    elif idx < 0:
        removed_elements += current_numbers[0]
        current_element = current_numbers[0]
        current_numbers[0] = current_numbers[-1]
        increase_and_decrease(current_element, current_numbers, idx)

    elif idx >= len(current_numbers):
        removed_elements += current_numbers[-1]
        current_element = current_numbers[-1]
        current_numbers[-1] = current_numbers[0]
        increase_and_decrease(current_element, current_numbers, idx)

print(removed_elements)