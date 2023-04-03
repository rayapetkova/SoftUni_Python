cards = input().split()
shuffles = int(input())

for i in range(shuffles):
    final_list = []
    half = len(cards) // 2
    left_half = cards[0:half]
    right_half = cards[half::]
    for j in range(len(left_half)):
        final_list.append(left_half[j])
        final_list.append(right_half[j])

    cards = final_list

print(cards)