pairs = int(input())

pair_sum = 0
all_pairs_sum = 0
max_diff = 0
previous_pair_sum = 0

for i in range(1, pairs + 1):
    number = float(input())
    number1 = float(input())
    pair_sum = number + number1

    all_pairs_sum = all_pairs_sum + pair_sum

    if all_pairs_sum != pairs * pair_sum:
        max_diff = abs(pair_sum - previous_pair_sum)
        previous_pair_sum = pair_sum

if all_pairs_sum == pairs * pair_sum:
    print(f"Yes, value={pair_sum:.0f}")
else:
    print(f"No, maxdiff={max_diff:.0f}")
