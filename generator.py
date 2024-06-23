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

def add_new_person():
    count = 1
    while count != 0:
        person_info = Person.generated_person()
        firstname = person_info.firstname
        email = person_info.email
        password = person_info.password

        count -= 1
        print(firstname, email, password)
        return [firstname, email, password]


add_new_person()