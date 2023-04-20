num = int(input())
reservations = set()

for i in range(num):
    guest = input()
    reservations.add(guest)

while True:
    line = input()
    if line == "END":
        break
    reservations.discard(line)

sorted_reservations = sorted(reservations)
# it is better to sort here and not in the loop, because the sorting will happen once.
# if we sort in the loop, the sorting will be happening on every iteration

print(len(reservations))
[print(person) for person in sorted_reservations]






#2
#
# num = int(input())
# reservations = set()
# people_who_attend = set()
#
# for i in range(num):
#     guest = input()
#     reservations.add(guest)
#
# while True:
#     line = input()
#     if line == "END":
#         break
#     people_who_attend.add(line)
#
# reservations -= people_who_attend
# sorted_reservations = sorted(reservations)
# # it is better to sort here and not in the loop, because the sorting will happen once.
# # if we sort in the loop, the sorting will be happening on every iteration
#
# print(len(reservations))
# [print(person) for person in sorted_reservations]
