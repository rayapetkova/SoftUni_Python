input_line = list(input())

numbers = [i for i in input_line if i.isdigit()]
text = [j for j in input_line if not j.isdigit()]

take_list = []
skip_list = []

taken_string = []


for j in range(len(numbers)):
    if j % 2 == 0:
        take_list.append(numbers[j])
    else:
        skip_list.append(numbers[j])

idx = 0

for first in take_list:
    taken_string.append(text[0:int(first)])
    del text[0:int(first)]
    del text[0:int(skip_list[idx])]
    idx += 1

final1 = []
final2 = []

for n in taken_string:
    final1.append("".join(n))

for i in final1:
    final2.append(i)

print("".join(final2))
