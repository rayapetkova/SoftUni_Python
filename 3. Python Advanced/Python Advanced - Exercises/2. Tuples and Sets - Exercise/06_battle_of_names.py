num = int(input())
odd_set, even_set = set(), set()

for i in range(1, num + 1):
    name = input()
    sum_ascii = 0
    for symbol in name:
        sum_ascii += ord(symbol)

    if int(sum_ascii / i) % 2 == 0:
        even_set.add(int(sum_ascii / i))
    else:
        odd_set.add(int(sum_ascii / i))

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_odd_set == sum_even_set:
    print(', '.join(str(el) for el in odd_set.union(even_set)))

elif sum_odd_set > sum_even_set:
    print(', '.join(str(el) for el in odd_set.difference(even_set)))

else:
    print(', '.join(str(el) for el in odd_set.symmetric_difference(even_set)))