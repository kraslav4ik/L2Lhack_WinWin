import pygsheets

c = pygsheets.authorize(client_secret='client_secret.json')

open_sheet = c.open('Новая форма (Ответы)')
wks = open_sheet[0]

values_mat = wks.get_all_values(returnas='matrix')

# print(values_mat)

class Volunteer(name):

    def __init__(self):
        self.name = name