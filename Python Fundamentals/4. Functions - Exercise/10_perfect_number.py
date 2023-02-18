def perfect_num(num):
    sum_nums = 0
    perfect = False
    for i in range(1, num):
        if num % i == 0:
            sum_nums += i
        if sum_nums == num:
            perfect = True
            break
    if perfect:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


current_num = int(input())
print(perfect_num(current_num))