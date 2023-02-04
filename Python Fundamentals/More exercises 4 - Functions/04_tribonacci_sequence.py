def tribonacci_sequence(num):
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    if num == 3:
        return "1 1 2"
    else:
        tribonacci_lst = [1, 1, 2]
        for i in range(num - 3):
            next_num = tribonacci_lst[i] + tribonacci_lst[i + 1] + tribonacci_lst[i + 2]
            tribonacci_lst.append(next_num)
        result = " ".join([str(j) for j in tribonacci_lst])
        return result


curr_num = int(input())
print(tribonacci_sequence(curr_num))