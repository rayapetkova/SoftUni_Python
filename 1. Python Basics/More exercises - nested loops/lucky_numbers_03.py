num = int(input())

sum_first_two = 0
sum_second_two = 0
equal = False

if num < 10:
    for i in range(1, num):
        for j in range(1, num):
            sum_first_two = i + j
            for k in range(1, num):
                for l in range(1, num):
                    sum_second_two = k + l
                    if sum_first_two == sum_second_two and sum_first_two == num and sum_second_two <= num:
                        equal = True
                    if equal:
                        if num % sum_first_two == 0 and num % sum_second_two == 0:
                            print(f"{i}{j}{k}{l}", end=" ")

else:
    for i in range(1, 10):
        for j in range(1, 10):
            sum_first_two = i + j
            for k in range(1, 10):
                for l in range(1, 10):
                    sum_second_two = k + l
                    if sum_first_two == sum_second_two and num % sum_first_two == 0 and num % sum_second_two == 0:
                        print(f"{i}{j}{k}{l}", end=" ")