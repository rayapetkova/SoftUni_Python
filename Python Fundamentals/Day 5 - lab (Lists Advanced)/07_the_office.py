employees = [int(j) for j in input().split()]
factor = int(input())

average = sum(employees) / len(employees)
happy_employees = list(filter(lambda x: x >= average, employees))

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")