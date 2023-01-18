import os
import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


def generated_file():
    #path = os.path.abspath(f"filetest{random.randint(0, 999)}.txt")
    relative_path = f"resources\\filetest{random.randint(0, 999)}.txt"

    abs_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), relative_path))

    with open(abs_path, 'w+') as file:
        file.write(f'Hello World{random.randint(0, 999)}')
    return file.name, abs_path
