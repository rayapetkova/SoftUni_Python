def happiness(employees_str):
    employees = list(map(int, employees_str))
    average = sum(employees) / len(employees)
    happy_employees = list(filter(lambda x: x >= average, employees))

    if len(happy_employees) >= len(employees) / 2:
        return f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!"
    else:
        return f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!"


curr_employees = input().split()
curr_factor = int(input())
print(happiness(curr_employees))
