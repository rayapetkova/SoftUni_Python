number = input()
number_list = [int(i) for i in number]
for j in range(len(number)):
    maxnum = max(number_list)
    print(maxnum, end='')
    number_list.remove(maxnum)