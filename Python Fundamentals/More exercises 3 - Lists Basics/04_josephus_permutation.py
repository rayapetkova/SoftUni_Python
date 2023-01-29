people = input().split()
k = int(input()) - 1
n = len(people)
new = []
num_in_people = 0
all_elements = ""

for i in range(1, len(people) + 1):
    while n > 0:
        num_in_people = (num_in_people + k) % n
        removed = people.pop(num_in_people)
        new.append(removed)
        n -= 1

new_integers = [int(j) for j in new]

for x in new:
    new_integers = ','.join(new)

print("[" + new_integers + "]")