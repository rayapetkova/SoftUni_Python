def sums(number):
    even_sum = 0
    odd_sum = 0
    for i in number:
        new_i = int(i)
        if new_i % 2 == 0:
            even_sum += new_i
        else:
            odd_sum += new_i
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


current_number = input()
sums(current_number)
