men = int(input())
women = int(input())
tables = int(input())

counter_couples = 0
done = False

for i in range(1, men + 1):
    for j in range(1, women + 1):
        counter_couples = counter_couples + 1
        print(f"({i} <-> {j})", end=" ")
        if counter_couples >= tables:
            done = True
            break
    if done:
        break