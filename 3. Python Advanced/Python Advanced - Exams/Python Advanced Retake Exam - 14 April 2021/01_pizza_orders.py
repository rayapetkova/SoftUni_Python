from collections import deque

orders = deque([int(n) for n in input().split(", ")])
employees = [int(n) for n in input().split(", ")]

total_pizzas = 0
while employees and orders:
    order, employee = orders.popleft(), employees.pop()
    if order > 10 or order <= 0:
        employees.append(employee)
        continue
    if order <= employee:
        total_pizzas += order
    elif order > employee:
        order -= employee
        total_pizzas += employee
        orders.appendleft(order)

if not orders:
    print(f"All orders are successfully completed!\nTotal pizzas made: {total_pizzas}\n"
          f"Employees: {', '.join(str(e) for e in employees)}")
elif not employees and orders:
    print(f"Not all orders are completed.\nOrders left: {', '.join(str(o) for o in orders)}")