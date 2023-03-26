def sum_even_digits(num):
    return sum(int(n) for n in num if n.isdigit() and int(n) % 2 == 0)


def sum_odd_digits(num):
    return sum(int(n) for n in num if n.isdigit() and int(n) % 2 != 0)


number = input()
print(sum_even_digits(number) * sum_odd_digits(number))