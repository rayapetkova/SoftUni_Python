import sys

numbers = int(input())

even_sum = 0
odd_sum = 0

even_max_number = -sys.maxsize
odd_max_number = -sys.maxsize
even_min_number = sys.maxsize
odd_min_number = sys.maxsize

for i in range(1, numbers + 1):
    num = float(input())
    if i % 2 == 0:
        even_sum = even_sum + num
        if num > even_max_number:
            even_max_number = num
        if num < even_min_number:
            even_min_number = num
        if i == 0:
            even_max_number = str("No")
            even_min_number = str("No")

    else:
        odd_sum = odd_sum + num
        if num > odd_max_number:
            odd_max_number = num
        if num < odd_min_number:
            odd_min_number = num


print(f"OddSum={odd_sum:.2f},")

if numbers == 0:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min_number:.2f},")

if numbers == 0:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max_number:.2f},")

print(f"EvenSum={even_sum:.2f},")

if numbers == 0:
    print(f"EvenMin=No,")
elif numbers == 1:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min_number:.2f},")

if numbers == 0:
    print(f"EvenMax=No")
elif numbers == 1:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max_number:.2f}")