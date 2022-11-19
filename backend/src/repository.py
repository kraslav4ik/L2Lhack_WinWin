from typing import List
from volunteer import Volunteer
from table_tools import TableTools


class Repository:

    def __init__(self):
        self.table_tools = TableTools()

    def get_all_cities(self) -> List[str]:
        return self.table_tools.get_all_cities()

    # def get_all_volunteers(self) -> List[Volunteer]:
    #     return [v.to_json() for v in self.volunteers]

    def get_volunteers_by_city(self, city) -> List[Volunteer]:
        return [v.to_json() for v in self.table_tools.get_volunteers_by_city(city)]

