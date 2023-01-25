first_num_st = int(input())
second_num_des = int(input())
third_num_ed = int(input())

j_flag = False

for i in range(1, first_num_st + 1):
    if i % 2 == 0:
        first_printed_num = i
        for j in range(1, second_num_des + 1):
            if j != 1 and j != 4 and j != 6 and j != 8 and j != 9:
                second_printed_num = j
                for k in range(1, third_num_ed + 1):
                    if k % 2 == 0:
                        third_printed_num = k
                        print(f"{first_printed_num} {second_printed_num} {third_printed_num}", end=" ")
                        print()