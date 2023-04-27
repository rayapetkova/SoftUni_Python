from collections import deque

times = deque(int(n) for n in input().split())
tasks = [int(n) for n in input().split()]
dictionary = {'Darth Vader Ducky': 0, 'Thor Ducky': 0, 'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}

while times and tasks:
    time = times.popleft()
    task = tasks.pop()
    result = time * task
    if 0 < result <= 60:
        dictionary['Darth Vader Ducky'] += 1
    elif 61 <= result <= 120:
        dictionary['Thor Ducky'] += 1
    elif 121 <= result <= 180:
        dictionary['Big Blue Rubber Ducky'] += 1
    elif 181 <= result <= 240:
        dictionary['Small Yellow Rubber Ducky'] += 1
    elif result > 240:
        task -= 2
        times.append(time)
        tasks.append(task)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, number in dictionary.items():
    print(f"{key}: {number}")