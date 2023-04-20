from collections import deque


def symbols_calculations(symbol, curr_bee, curr_nectar):
    if symbol == "+":
        return curr_bee + curr_nectar
    elif symbol == "-":
        return curr_bee - curr_nectar
    elif symbol == "*":
        return curr_bee * curr_nectar
    elif symbol == "/":
        return curr_bee / curr_nectar


bees = deque([int(el) for el in input().split()])
nectar_stack = [int(el) for el in input().split()]
symbols = deque(input().split())
total_honey_made = 0

while bees and nectar_stack:
    bee, nectar = bees.popleft(), nectar_stack.pop()
    if nectar >= bee:
        if nectar > 0:
            result = symbols_calculations(symbols.popleft(), bee, nectar)
            total_honey_made += abs(result)
    else:
        bees.appendleft(bee)

print(f"Total honey made: {total_honey_made}")
if bees:
    print(f"Bees left: {', '.join(str(some_bee) for some_bee in bees)}")
if nectar_stack:
    print(f"Nectar left: {', '.join(str(some_nectar) for some_nectar in nectar_stack)}")
