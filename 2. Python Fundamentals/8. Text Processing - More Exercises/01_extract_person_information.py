num = int(input())

for _ in range(num):
    text = input()
    idx_first_symbol = text.index("@")
    idx_second_symbol = text.index("|")
    name = text[idx_first_symbol + 1:idx_second_symbol]

    idx_third_symbol = text.index("#")
    idx_fourth_symbol = text.index("*")
    age = text[idx_third_symbol + 1:idx_fourth_symbol]
    print(f"{name} is {age} years old.")