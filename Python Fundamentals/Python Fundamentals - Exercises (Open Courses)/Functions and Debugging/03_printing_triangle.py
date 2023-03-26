def second_part_creating(num):
    result = []
    for i in range(1, num + 1):
        result.append(str(i))
    for n in range(len(result) - 1, -1, -1):
        final = result[:n + 1]
        print(" ".join(final))


def first_part_creating(num):
    result = []
    for i in range(1, num + 1):
        result.append(str(i))
    for n in range(len(result) - 1):
        final = result[:n + 1]
        print(" ".join(final))


number = int(input())
first_part_creating(number)
second_part_creating(number)