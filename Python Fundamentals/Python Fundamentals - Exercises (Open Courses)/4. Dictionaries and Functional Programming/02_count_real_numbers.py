numbers = list(map(float, input().split()))
dictionary = {}

for num in numbers:
    dictionary[num] = dictionary.get(num, 0) + 1

for key, value in sorted(dictionary.items(), key=lambda x: x[0]):
    print(f"{key} -> {value} times")