text = [int(j) for j in input().split(", ")]

for i in text:
    if i == 0:
        text.remove(i)
        text.append(i)

print(text)





#2

# text = [int(j) for j in input().split(", ")]
#
# for i in text:
#     if i == 0:
#         text.append(text.pop(text.index(i)))
#
# print(text)





#3

# text = [int(j) for j in input().split(", ")]
#
# for i in text:
#     if i == 0:
#         first = text.index(i)
#         second = text.pop(first)
#         text.append(second)
#
# print(text)