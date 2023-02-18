def office_chairs(rooms):
    chairs_total = 0
    people_total = 0
    for i in range(rooms):
        one_room = input().split()
        chairs = int(len(one_room[0]))
        people = int(one_room[1])
        if chairs >= people:
            chairs_total += chairs
            people_total += people
        else:
            chairs_total += chairs
            people_total += people
            print(f"{people - chairs} more chairs needed in room {i + 1}")
    if chairs_total >= people_total:
        print(f"Game On, {chairs_total - people_total} free chairs left")


current_rooms = int(input())
office_chairs(current_rooms)