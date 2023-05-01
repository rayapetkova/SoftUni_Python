from collections import deque

seats = input().split(", ")
first_numbers = deque(int(n) for n in input().split(", "))
second_numbers = deque(int(n) for n in input().split(", "))

seat_matches, rotations = [], 0

while len(seat_matches) < 3 and rotations < 10:
    first, second = first_numbers.popleft(), second_numbers.pop()
    result = first + second
    if f"{first}{chr(result)}" in seats:
        seat_matches.append(f"{first}{chr(result)}")
        seats.remove(f"{first}{chr(result)}")
    elif f"{second}{chr(result)}" in seats:
        seat_matches.append(f"{second}{chr(result)}")
        seats.remove(f"{second}{chr(result)}")
    else:
        first_numbers.append(first)
        second_numbers.appendleft(second)
    rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}\nRotations count: {rotations}")
