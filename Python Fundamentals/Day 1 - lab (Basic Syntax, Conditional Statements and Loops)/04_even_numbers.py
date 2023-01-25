n = int(input())
even_flag = False

for i in range(1, n + 1):
    number = float(input())
    if number % 2 != 0:
        print(f"{number:.0f} is odd!")
        exit()
    else:
        even_flag = True

if even_flag:
    print("All numbers are even.")