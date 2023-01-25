start_number = int(input())
finish_number = int(input())

for i in range(start_number, finish_number + 1):
    for j in range(start_number, finish_number + 1):
        for k in range(start_number, finish_number + 1):
            sum_j_k = j + k
            for l in range(start_number, i):
                if ((i % 2 == 0 and l % 2 != 0) or (i % 2 != 0 and l % 2 == 0)) and i > l and sum_j_k % 2 == 0:
                    print(f"{i}{j}{k}{l}", end=" ")