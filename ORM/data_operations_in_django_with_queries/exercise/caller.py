import os
import django

from helpers import populate_model_with_data

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name, species):
    pet = Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name, origin, age, description, is_magical):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(l) for l in locations)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    for car in Car.objects.all():
        discount = sum(int(n) for n in str(car.year)) / 100
        car.price_with_discount = float(car.price) - (float(car.price) * float(discount))
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values("model", "price_with_discount")


def delete_last_car():
    car = Car.objects.last()
    car.delete()


def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)

    return '\n'.join(str(t) for t in tasks)


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 == 1:
            task.is_finished = True
            task.save()


def encode_and_replace(text, task_title):
    tasks = Task.objects.filter(title=task_title)

    encoded_text = ''.join(chr(ord(l) - 3) for l in text)

    for task in tasks:
        task.description = encoded_text
        task.save()


def get_deluxe_room():
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    return '\n'.join(str(r) for r in deluxe_rooms)


def increase_room_capacity():
    previous_room = None

    for room in HotelRoom.objects.all().order_by("id"):
        if not room.is_reserved:
            continue
        if previous_room is None:
            room.capacity += room.id
        else:
            room.capacity += previous_room

        previous_room = room.capacity
        room.save()


def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room():
    room = HotelRoom.objects.last()

    if room.is_reserved:
        room.delete()


def update_characters():
    for char in Character.objects.all():
        if char.class_name == "Mage":
            char.level += 3
            char.intelligence -= 7

        elif char.class_name == "Warrior":
            char.hit_points /= 2
            char.dexterity += 4

        elif char.class_name in ["Assassin", "Scout"]:
            char.inventory = "The inventory is empty"

        char.save()


def fuse_characters(first, second):
    name = first.name + " " + second.name
    class_name = "Fusion"
    level = (first.level + second.level) // 2
    strength = (first.strength + second.strength) * 1.2
    dexterity = (first.dexterity + second.dexterity) * 1.4
    intelligence = (first.intelligence + second.intelligence) * 1.5
    hit_points = (first.hit_points + second.hit_points)

    if first.class_name in ["Mage", "Scout"]:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory
    )
    first.delete()
    second.delete()


def grand_dexterity():
    Character.objects.all().update(dexterity=30)


def grand_intelligence():
    Character.objects.all().update(intelligence=40)


def grand_strength():
    Character.objects.all().update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()

delete_characters()
