import datetime
from typing import List, Optional
from volunteer import Volunteer
from constants import *
import csv

import pygsheets

HELP_OPTIONS = [COMMON, LEGAL, SHELTER, GUIDE, JOB, PSYCHO, LANGUAGE, BANK, RENT]

use_cache = False


class TableTools:

    def __init__(self):
        c = pygsheets.authorize(client_secret='./backend/data/client_secret.json')
        open_sheet = c.open('Volunteers form')
        self.wks = open_sheet.sheet1
        self.cities = [None, []]
        self.volunteers = [None, []]

    def get_all_cities(self) -> List[str]:
        now = datetime.datetime.now()
        if use_cache:
            if self.cities[0] is None or (now - self.cities[0]).total_seconds() / 60 > 5:
                self.cities[1] = self.fetch_all_cities()
                self.cities[0] = now
            return self.volunteers[1]
        return self.fetch_all_cities()

    def fetch_all_cities(self) -> List[str]:

        cities = set()
        for v in self.get_all_volunteers():
            cities.add(v.city)
        return list(cities)

    def get_volunteers_by_city(self, city: Optional[str]):
        if city is None:
            return self.get_all_volunteers()
        return [v for v in self.get_all_volunteers() if v.city == city]


    def get_all_volunteers(self):
        now = datetime.datetime.now()
        if use_cache:
            if self.volunteers[0] is None or (now - self.volunteers[0]).total_seconds() / 60 > 5:
                self.volunteers[1] = self.fetch_all_volunteers()
                self.volunteers[0] = now

            return self.volunteers[1]
        return self.fetch_all_volunteers()

    def fetch_all_volunteers(self):
        filepath = './backend/data/'
        filename = 'table_data'
        self.wks.export(pygsheets.ExportType.CSV, filename,  filepath)
        with open(filepath + filename + '.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            volunteers = []
            for i, row in enumerate(reader):
                if i == 0 or not row[0]:
                    continue
                if row[10] == 'FALSE':
                    continue
                help_options_from_table = row[6]
                help_options = []
                for option in HELP_OPTIONS:
                    if help_options_from_table.find(option) != -1:
                        help_options.append(option)
                sex = "Not specified"
                sex_value = row[8]
                if '??' in sex_value or 'F' in sex_value or 'w' in sex_value:
                    sex = "FEMALE"
                if '??' in sex_value or 'M' in sex_value:
                    sex = "MALE"
                volunteers.append(Volunteer(row[3], row[4], row[2], row[5], help_options, row[7], sex, row[9]))
            return volunteers

