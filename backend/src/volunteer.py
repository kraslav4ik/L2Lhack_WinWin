from typing import List


class Volunteer:

    def __init__(self, name: str, email: str, city: str, telegram: str, help_options : List[str], description: str):
        self.name = name
        self.city = city
        self.email = email
        self.telegram = telegram
        self.help_options = help_options
        self.description = description

    def to_json(self):
        return self.__dict__
