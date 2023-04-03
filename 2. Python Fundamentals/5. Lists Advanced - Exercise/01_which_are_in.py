def find_words(first, second):
    lst = []
    for i in first:
        for j in second:
            if i in j:
                lst.append(i)
                break
    return lst


current_first = input().split(", ")
current_second = input().split(", ")
print(find_words(current_first, current_second))
