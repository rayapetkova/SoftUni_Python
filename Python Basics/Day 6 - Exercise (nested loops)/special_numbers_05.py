num = int(input())

for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        for k in range (1, 9 + 1):
            for l in range(1, 9 + 1):
                if num % i == 0 and num % j == 0 and num % k == 0 and num % l == 0:
                    print(f"{i}{j}{k}{l}", end=" ")