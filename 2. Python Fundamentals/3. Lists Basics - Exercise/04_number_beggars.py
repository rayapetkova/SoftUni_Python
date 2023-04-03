coins = [int(j) for j in input().split(", ")]
beggars = int(input())
lists = [0] * beggars
count = 0

for i in coins:
    lists[count] += i
    count += 1
    if count == beggars:
        count = 0

print(lists)