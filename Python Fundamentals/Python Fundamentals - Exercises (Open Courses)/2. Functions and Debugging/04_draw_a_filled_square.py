def first_and_last_row(num):
    return f"--" * num


def fill(num):
    return "-" + f"\/" * (num - 1) + "-"


number = int(input())
print(first_and_last_row(number))
for n in range(number - 2):
    print(fill(number))
print(first_and_last_row(number))