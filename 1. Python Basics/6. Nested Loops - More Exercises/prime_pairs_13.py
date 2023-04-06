first_num = int(input())
second_num = int(input())
first_diff = int(input())
second_diff = int(input())

for i in range(first_num, (first_num + first_diff) + 1):
    for j in range(second_num, second_num + second_diff + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and j % 2 != 0 and j % 3 != 0 and j % 5 != 0 and j % 7 != 0:
            print(f"{i}{j}")