num = int(input())
free_chairs = 0
need_chairs = False

for i in range(1, num + 1):
    line = input().split()
    chairs, visitors = len(line[0]), int(line[1])
    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {i}")
        need_chairs = True
    elif visitors < chairs:
        free_chairs += chairs - visitors

if not need_chairs:
    print(f"Game On, {free_chairs} free chairs left")





#2
#
# def office_chairs(rooms):
#     chairs_total = 0
#     people_total = 0
#     for i in range(rooms):
#         one_room = input().split()
#         chairs = int(len(one_room[0]))
#         people = int(one_room[1])
#         if chairs >= people:
#             chairs_total += chairs
#             people_total += people
#         else:
#             chairs_total += chairs
#             people_total += people
#             print(f"{people - chairs} more chairs needed in room {i + 1}")
#     if chairs_total >= people_total:
#         print(f"Game On, {chairs_total - people_total} free chairs left")
#
#
# current_rooms = int(input())
# office_chairs(current_rooms)
