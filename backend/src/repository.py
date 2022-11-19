from typing import List
from volunteer import Volunteer


class Repository:

    def __init__(self, cities, volunteers):
        self.cities = cities
        self.volunteers = volunteers

    def get_all_cities(self) -> List[str]:
        return self.cities

    # def get_all_volunteers(self) -> List[Volunteer]:
    #     return [v.to_json() for v in self.volunteers]

    def get_volunteers_by_city(self, city) -> List[Volunteer]:
        return [v.to_json() for v in self.volunteers if v.city == city]

