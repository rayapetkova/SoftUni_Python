num = int(input())
final = []

for i in range(num):
    line = input().split("-")
    first_range, second_range = line[0].split(","), line[1].split(",")
    first_start, first_end = int(first_range[0]), int(first_range[1])
    second_start, second_end = int(second_range[0]), int(second_range[1])
    first_set, second_set = set(), set()

    for j in range(first_start, first_end + 1):
        first_set.add(j)

    for k in range(second_start, second_end + 1):
        second_set.add(k)

    final.append(first_set.intersection(second_set))

max_length_set = max(len(lst_nums) for lst_nums in final)
longest_intersection = ''

for some_set in final:
    if len(some_set) == max_length_set:
        longest_intersection = list(some_set)

print(f"Longest intersection is {longest_intersection} with length {max_length_set}")
