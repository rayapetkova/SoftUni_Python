from collections import deque

tools = deque([int(n) for n in input().split()])
substances = [int(n) for n in input().split()]

challenges = [int(n) for n in input().split()]

while tools and substances and challenges:
    tool, substance = tools.popleft(), substances.pop()

    value = tool * substance

    if value in challenges:
        challenges.remove(value)

    else:
        tool += 1
        tools.append(tool)

        substance -= 1
        if substance == 0:
            continue

        substances.append(substance)

if (not tools or not substances) and challenges:
    print(f"Harry is lost in the temple. Oblivion awaits him.")

if not challenges:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(t) for t in tools)}")
if substances:
    print(f"Substances: {', '.join(str(s) for s in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(c) for c in challenges)}")
