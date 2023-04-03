numbers = [int(i) for i in input().split()]

even_nums = []
odd_nums = []

max_even_nums = []
max_odd_nums = []

min_even_nums = []
min_odd_nums = []

while True:
    command = input()
    if command == "end":
        print(numbers)
        exit()

    command = command.split()

    if "exchange" in command:
        index = int(command[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
            continue
        else:
            first_half = numbers[0:index + 1]
            second_half = numbers[index + 1::]
            numbers = second_half + first_half

    elif "max" in command:
        if command[1] == "even":
            for num in numbers:
                if num % 2 == 0:
                    even_nums.append(num)
            if len(even_nums) > 0:
                max_even_num = max(even_nums)
                counter = numbers.count(max_even_num)
                if counter == 1:
                    print(numbers.index(max_even_num))
                elif counter > 1:
                    reversed_list = list(reversed(numbers))
                    for num in reversed_list:
                        if num % 2 == 0:
                            max_even_nums.append(num)
                    even_max = max(max_even_nums)
                    needed_num = (len(numbers) - 1) - reversed_list.index(even_max)
                    print(needed_num)
            else:
                print("No matches")
        elif command[1] == "odd":
            for num in numbers:
                if num % 2 != 0:
                    odd_nums.append(num)
            if len(odd_nums) > 0:
                max_odd_num = max(odd_nums)
                counter = numbers.count(max_odd_num)
                if counter == 1:
                    print(numbers.index(max_odd_num))
                elif counter > 1:
                    reversed_list = list(reversed(numbers))
                    for num in reversed_list:
                        if num % 2 != 0:
                            max_odd_nums.append(num)
                    odd_max = max(max_odd_nums)
                    needed_num = (len(numbers) - 1) - reversed_list.index(odd_max)
                    print(needed_num)
            else:
                print("No matches")

    elif "min" in command:
        if command[1] == "even":
            for num1 in numbers:
                if num1 % 2 == 0:
                    even_nums.append(num1)
            if len(even_nums) > 0:
                min_even_num = min(even_nums)
                counter1 = numbers.count(min_even_num)
                if counter1 == 1:
                    print(numbers.index(min_even_num))
                elif counter1 > 1:
                    reversed_list = list(reversed(numbers))
                    for num in reversed_list:
                        if num % 2 == 0:
                            min_even_nums.append(num)
                    even_min = min(min_even_nums)
                    needed_num = (len(numbers) - 1) - reversed_list.index(even_min)
                    print(needed_num)
            else:
                print("No matches")
        elif command[1] == "odd":
            for num1 in numbers:
                if num1 % 2 != 0:
                    odd_nums.append(num1)
            if len(odd_nums) > 0:
                min_odd_num = min(odd_nums)
                counter1 = numbers.count(min_odd_num)
                if counter1 == 1:
                    print(numbers.index(min_odd_num))
                elif counter1 > 1:
                    reversed_list = list(reversed(numbers))
                    for num in reversed_list:
                        if num % 2 != 0:
                            min_odd_nums.append(num)
                    odd_min = min(min_odd_nums)
                    needed_num = (len(numbers) - 1) - reversed_list.index(odd_min)
                    print(needed_num)
            else:
                print("No matches")

    elif "first" in command:
        number = int(command[1])
        if number > len(numbers) or number < 0:
            print("Invalid count")
            continue
        if command[2] == "even":
            result = [i for i in numbers if i % 2 == 0][0:number]
            print(result)
        elif command[2] == "odd":
            result = [i for i in numbers if i % 2 != 0][0:number]
            print(result)

    elif "last" in command:
        number = int(command[1])
        if number > len(numbers) or number < 0:
            print("Invalid count")
            continue
        if command[2] == "even":
            reversed_numbers = list(reversed(numbers))
            result = [j for j in reversed_numbers if j % 2 == 0][0:number]
            print(result[::-1])
        elif command[2] == "odd":
            reversed_numbers = list(reversed(numbers))
            result = [j for j in reversed_numbers if j % 2 != 0][0:number]
            print(result[::-1])
