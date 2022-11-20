from typing import List


class Volunteer:

    def __init__(self, name: str, city: str, email: str, telegram: str, help_options: List[str], description: str,
                 sex: str, age: str):
        self.name = name
        self.city = city
        self.email = email
        self.telegram = telegram
        self.help_options = help_options
        self.description = description
        self.sex = sex
        self.age = age


    def to_json(self):
        # print(self.__dict__)
        return self.__dict__
