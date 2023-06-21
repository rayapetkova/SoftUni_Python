num = int(input())
set_car_plates = set()

for i in range(num):
    direction, car_plate = input().split(", ")
    if direction == "IN":
        set_car_plates.add(car_plate)
    else:
        set_car_plates.discard(car_plate)
        # we can also use .remove(), but this will receive an error if the car plate doesn't exist
        # it doesn't matter if we use .discard() or .remove() in this task

if not set_car_plates:
    print(f"Parking Lot is Empty")
else:
    [print(plate) for plate in set_car_plates]
