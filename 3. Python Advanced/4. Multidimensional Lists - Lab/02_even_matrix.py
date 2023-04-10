rows = int(input())
final = []

for i in range(rows):
    numbers = [int(n) for n in input().split(", ") if int(n) % 2 == 0]
    final.append(numbers)

print(final)





#2
#
# rows = int(input())
#
# print([[int(n) for n in input().split(", ") if int(n) % 2 == 0] for i in range(rows)])
