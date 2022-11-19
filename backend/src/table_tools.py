from typing import List
from volunteer import Volunteer
from constants import *

import pygsheets

HELP_OPTIONS = [LIFE, LEGAL, JOB, BED, CHAT, GUIDE, LEARN, EXPERIENCE, WORK, DONAT, PSYCHO]


CITY_COLUMN = 'E'
NAME_COLUMN = 'D'
EMAIL_COLUMN = 'C'
TELEGRAM_COLUMN = 'F'
HELP_OPTIONS_COLUMN = 'G'
DESCRIPTION_COLUMN = 'H'
START_ROW = 2


class TableTools:

    def __init__(self):
        c = pygsheets.authorize(client_secret='../data/client_secret.json')
        open_sheet = c.open('Volunteers form')
        self.wks = open_sheet.sheet1

    def get_all_cities(self) -> List[str]:
        city_string = '---'
        i = START_ROW
        cities = set()
        while city_string:
            city_string = self.wks.cell(f'{CITY_COLUMN}{i}').value
            if city_string:
                cities.add(city_string)
            i += 1
        return list(cities)

    def get_volunteers_by_city(self, city: str):
        city_string = '---'
        i = START_ROW
        suitable_rows = []
        while city_string:
            city_string = self.wks.cell(f'{CITY_COLUMN}{i}').value
            if city_string and city_string == city:
                suitable_rows.append(i)
            i += 1
        volunteers = []
        for row in suitable_rows:
            volunteers.append(self.create_volunteer(row))
        return volunteers

    def create_volunteer(self, row: int) -> Volunteer:
        help_options = []
        help_options_from_table = self.wks.cell(f'{HELP_OPTIONS_COLUMN}{row}').value
        for option in HELP_OPTIONS:
            if help_options_from_table.find(option) != -1:
                help_options.append(option)
        return Volunteer(
            self.wks.cell(f'{NAME_COLUMN}{row}').value, self.wks.cell(f'{CITY_COLUMN}{row}').value,
            self.wks.cell(f'{EMAIL_COLUMN}{row}').value, self.wks.cell(f'{TELEGRAM_COLUMN}{row}').value,
            help_options, self.wks.cell(f'{DESCRIPTION_COLUMN}{row}').value
        )


