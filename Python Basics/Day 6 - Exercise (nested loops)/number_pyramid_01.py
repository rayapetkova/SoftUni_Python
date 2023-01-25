num = int(input())

current_num = 1

done = False

for row in range(1, num + 1):
    for column in range(1, row + 1):
        print(current_num, end=' ')
        if current_num == num:
            done = True
            break
        current_num += 1
    if done:
        break
    print()