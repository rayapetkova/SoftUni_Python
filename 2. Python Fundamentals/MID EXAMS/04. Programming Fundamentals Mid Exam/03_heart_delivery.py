numbers = [int(i) for i in input().split("@")]

idx = 0

while True:
    line = input()
    if line == "Love!":
        break

    command = line.split()
    length = int(command[1])
    if idx + length >= len(numbers):
        idx = 0
    else:
        idx += length
    if numbers[idx] > 2:
        numbers[idx] -= 2
    elif numbers[idx] == 2 or numbers[idx] == 1:
        numbers[idx] -= 2
        print(f"Place {idx} has Valentine's day.")
        continue
    elif numbers[idx] == 0:
        print(f"Place {idx} already had Valentine's day.")

print(f"Cupid's last position was {idx}.")
if numbers.count(0) == len(numbers):
    print(f"Mission was successful.")
else:
    counter = [int(i) for i in numbers if i != 0]
    print(f"Cupid has failed {len(counter)} places.")