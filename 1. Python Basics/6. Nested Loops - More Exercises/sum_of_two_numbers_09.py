start_num = int(input())
finish_num = int(input())
magic_num = int(input())

counter = 0
found = False

for i in range(start_num, finish_num + 1):
    for j in range(start_num, finish_num + 1):
        counter = counter + 1
        sum_nums = i + j
        if sum_nums == magic_num:
            print(f"Combination N:{counter} ({i} + {j} = {magic_num})")
            found = True
            break
    if found:
        break
if found == False:
    print(f"{counter} combinations - neither equals {magic_num}")