n = int(input())
all_nums = []
even_nums = []
odd_nums = []
negative_nums = []
positive_nums = []
evens = False
odds = False
negatives = False
positives = False

for i in range(n):
    number = int(input())
    all_nums.append(number)

text = input()

for j in all_nums:
    if text == "even":
        if j % 2 == 0:
            even_nums.append(j)
            evens = True
    elif text == "odd":
        if j % 2 != 0:
            odd_nums.append(j)
            odds = True
    elif text == "negative":
        if j < 0:
            negative_nums.append(j)
            negatives = True
    elif text == "positive":
        if j >= 0:
            positive_nums.append(j)
            positives = True

if evens:
    print(even_nums)
elif odds:
    print(odd_nums)
elif negatives:
    print(negative_nums)
elif positives:
    print(positive_nums)