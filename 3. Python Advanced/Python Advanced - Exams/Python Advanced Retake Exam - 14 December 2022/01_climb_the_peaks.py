from collections import deque

daily_portions = [int(n) for n in input().split(", ")]
daily_stamina = deque(int(n) for n in input().split(", "))

dictionary = {
    1: ('Vihren', 80),
    2: ('Kutelo', 90),
    3: ('Banski Suhodol', 100),
    4: ('Polezhan', 60),
    5: ('Kamenitza', 70)
}

idx, all_peaks = 1, []
days = 0
while True:
    if len(all_peaks) == 5 or days == 7:
        break
    food, stamina = daily_portions.pop(), daily_stamina.popleft()
    total = food + stamina
    if total >= dictionary[idx][1]:
        all_peaks.append(dictionary[idx][0])
        idx += 1
    days += 1

if len(all_peaks) == 5:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if all_peaks:
    print(f"Conquered peaks:")
    for peak in all_peaks:
        print(peak)