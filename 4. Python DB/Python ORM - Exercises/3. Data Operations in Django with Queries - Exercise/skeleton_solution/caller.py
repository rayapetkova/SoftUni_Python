import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions
def create_pet(name: str, species: str):
    Pet.objects.create(name=name, species=species)

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    all_locations = Location.objects.all().order_by('-id')

    return '\n'.join(f"{l.name} has a population of {l.population}!" for l in all_locations)


def new_capital():
    first_location = Location.objects.get(id=1)
    first_location.is_capital = True

    first_location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.get(id=1).delete()


def apply_discount():
    all_cars = Car.objects.all()

    for car in all_cars:
        car.price_with_discount = (1 - sum([int(d) for d in str(car.year)]) / 100) * float(car.price)

    Car.objects.bulk_update(all_cars, ['price_with_discount'])


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
    last_car = Car.objects.all().last()
    last_car.delete()


def show_unfinished_tasks():
    all_unfinished_tasks = Task.objects.filter(is_finished=False)

    return [f"Task - {t.title} needs to be done until {t.due_date}!" for t in all_unfinished_tasks]


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):
    encoded_text = "".join([chr(ord(s) - 3) for s in text])

    Task.objects.filter(title=task_title).update(description=encoded_text)


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    deluxe_rooms = [dr for dr in deluxe_rooms if dr.id % 2 == 0]
    return '\n'.join([f"Deluxe room with number {r.room_number} costs {r.price_per_night}$ per night!" for r in deluxe_rooms])


def increase_room_capacity():
    all_rooms = HotelRoom.objects.all().order_by('id')

    for i in range(len(all_rooms)):
        room = all_rooms[i]

        if not room.is_reserved:
            continue

        if i == 0:
            room.capacity += room.id
        else:
            room.capacity += HotelRoom.objects.get(id=room.id - 1).capacity

        room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.all().first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.all().last()

    if last_room.is_reserved:
        last_room.delete()


def update_characters():
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty"
    )


def fuse_characters(first_character: Character, second_character: Character):
    f_name = f"{first_character.name} {second_character.name}"
    f_class_name = "Fusion"
    f_level = (first_character.level + second_character.level) // 2
    f_strength = (first_character.strength + second_character.strength) * 1.2
    f_dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    f_intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    f_hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ["Mage", "Scout"]:
        f_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        f_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=f_name,
        class_name=f_class_name,
        level=f_level,
        strength=f_strength,
        dexterity=f_dexterity,
        intelligence=f_intelligence,
        hit_points=f_hit_points,
        inventory=f_inventory
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))

# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
#
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())

# apply_discount()
# print(get_recent_cars())

# encode_and_replace("Zdvk#wkh#glvkhv$", "Sample Task")
# print(Task.objects.get(title ='Sample Task') .description)

# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=101).is_reserved)
# increase_room_capacity()

# character1 = Character.objects.create(
#     name="Gandalf",
#     class_name="Mage",
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory="Staff of Magic, Spellbook",
# )
#
# character2 = Character.objects.create(
#     name="Hector",
#     class_name="Warrior",
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory="Sword of Troy, Shield of Protection",
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
