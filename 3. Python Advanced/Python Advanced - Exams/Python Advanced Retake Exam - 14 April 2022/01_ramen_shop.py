from collections import deque

bowls = [int(n) for n in input().split(", ")]
customers = deque(int(n) for n in input().split(", "))

while bowls and customers:
    bowl, customer = bowls.pop(), customers.popleft()
    if bowl > customer:
        bowl -= customer
        bowls.append(bowl)
    elif customer > bowl:
        customer -= bowl
        customers.appendleft(customer)

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(n) for n in bowls)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(n) for n in customers)}")