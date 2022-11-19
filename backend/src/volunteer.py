
class Volunteer:

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def to_json(self):
        return self.__dict__