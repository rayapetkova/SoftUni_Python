text = input()

numbers_list = [int(el) for el in text if el.isdigit()]
non_numbers_list = [el for el in text if not el.isdigit()]

take_list = [int(numbers_list[i]) for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [int(numbers_list[i]) for i in range(len(numbers_list)) if i % 2 != 0]

needed_string = []
idx = 0

for i in range(len(take_list)):
    needed_string.append(non_numbers_list[:take_list[i]])
    del non_numbers_list[:take_list[i]]
    del non_numbers_list[:skip_list[i]]

full_list = []
final = []

for nested_list in needed_string:
    full_list.append("".join(nested_list))

for element in full_list:
    final.append(element)

print("".join(final))