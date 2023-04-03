first, second = input().split()

min_word = min(len(first), len(second))
total = 0

for i in range(0, min_word):
    total += ord(first[i]) * ord(second[i])

if len(first) > len(second):
    for i in range(min_word, len(first)):
        total += ord(first[i])
elif len(first) < len(second):
    for i in range(min_word, len(second)):
        total += ord(second[i])
print(total)





# 2
# first, second = input().split()
# flag = False
# min_word = min(len(first), len(second))
# max_word = ""
#
# if len(first) > len(second):
#     flag = True
#     max_word = first
# elif len(first) < len(second):
#     flag = True
#     max_word = second
# else:
#     max_word = min_word
#
# total = 0
#
# for i in range(0, min_word):
#     total += ord(first[i]) * ord(second[i])
#
# if flag:
#     for j in range(min_word, len(max_word)):
#         total += ord(max_word[j])
# print(total)
