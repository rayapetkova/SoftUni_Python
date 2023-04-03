numbers = [int(i) for i in input().split()]
shot_targets = 0

while True:
    line = input()
    if line == "End":
        break
    idx = int(line)
    if 0 <= idx < len(numbers):
        num = int(numbers[idx])
        numbers[idx] = -1
        shot_targets += 1
        for i in range(len(numbers)):
            if numbers[i] != -1:
                if numbers[i] > num:
                    numbers[i] -= num
                else:
                    numbers[i] += num

nums = " ".join(str(x) for x in numbers)
print(f"Shot targets: {shot_targets} -> {nums}")