first_num = int(input())
second_num = int(input())
third_num = int(input())

for i in range(1, first_num + 1):
    if i % 2 == 0:
        first_printed_num = i
        counter = 0
        for j in range(2, second_num + 1):
            if j != 4 and j != 6 and j != 8 and j != 9:
                second_printed_num = j
                for k in range(1, third_num + 1):
                    if k % 2 == 0:
                        third_printed_num = k
                        print(f"{first_printed_num} {second_printed_num} {third_printed_num}", end=" ")
                        print()