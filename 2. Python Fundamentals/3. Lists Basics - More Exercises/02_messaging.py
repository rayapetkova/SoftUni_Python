numbers = input().split()
text = list(input())
new_string = ""


for i in range(len(numbers)):
    digits_sum = 0
    for number in numbers[i]:
        digit = int(number)
        digits_sum += digit
    if digits_sum > len(text) - 1:
        new_index = digits_sum % len(text)
        new_string += text[new_index]
        text.pop(new_index)

    else:
        new_string += text[digits_sum]
        text.pop(digits_sum)

print(new_string)