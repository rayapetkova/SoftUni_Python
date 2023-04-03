def symbols(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


current_a = input()
current_b = input()
symbols(current_a, current_b)