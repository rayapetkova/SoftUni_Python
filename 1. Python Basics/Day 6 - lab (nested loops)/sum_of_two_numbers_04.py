start_number = int(input())
finish_number = int(input())
magic_number = int(input())

combinations = 0
combination_found = False

for num in range(start_number, finish_number + 1):
    for num1 in range(start_number, finish_number + 1):
        combinations += 1
        if num + num1 == magic_number:
            print(f"Combination N:{combinations} ({num} + {num1} = {magic_number})")
            combination_found = True
            break

    if combination_found:
        break

if combination_found == False:
    print(f"{combinations} combinations - neither equals {magic_number}")