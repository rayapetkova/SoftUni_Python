numbers = [float(n) for n in input().split()]
dictionary = {}

for num in numbers:
    dictionary[num] = numbers.count(num)

for key, value in dictionary.items():
    print(f"{key:.1f} - {value} times")





#2
#
# numbers = tuple(map(float, input().split()))
# dictionary_nums = {}

# for num in numbers:
#     dictionary_nums[num] = numbers.count(num)

# for n, times in dictionary_nums.items():
#     print(f"{n} - {times} times")





#3
#
# numbers = tuple(map(float, input().split()))
# dictionary_nums = {}
#
# for num in numbers:
#     dictionary_nums[num] = dictionary_nums.get(num, 0) + 1
#
# for n, times in dictionary_nums.items():
#     print(f"{n} - {times} times")





#4
#
# numbers = tuple(map(float, input().split()))
# final = []
#
# for num in numbers:
#     if f"{num:.1f} - {numbers.count(num)} times" not in final:
#         final.append(f"{num:.1f} - {numbers.count(num)} times")
#
# for element in final:
#     print(element)
