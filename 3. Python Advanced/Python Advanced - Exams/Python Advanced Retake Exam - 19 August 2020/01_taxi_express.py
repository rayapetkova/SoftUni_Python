from collections import deque

customers = deque([int(n) for n in input().split(", ")])
taxis = [int(n) for n in input().split(", ")]

total_time = 0

while customers and taxis:
    customer, taxi = customers.popleft(), taxis.pop()

    if taxi >= customer:
        total_time += customer

    else:
        customers.appendleft(customer)

if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")

if not taxis and customers:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(str(c) for c in customers)}")
