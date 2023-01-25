number = int(input())
sum_nums = 0

while True:
    num = int(input())
    sum_nums = sum_nums + num

    if sum_nums >= number:
        break
print(sum_nums)