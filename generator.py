from faker import Faker
from dataclasses import dataclass

faker_ru = Faker('ru_RU')
Faker.seed()
@dataclass
class Person:
    firstname: str = None
    password: str = None
    email: str = None
    @staticmethod
    def generated_person():
        return Person(
            firstname=faker_ru.first_name(),
            password=faker_ru.password(),
            email=faker_ru.email()
        )



