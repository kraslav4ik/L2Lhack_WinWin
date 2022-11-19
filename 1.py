import pygsheets

c = pygsheets.authorize(client_secret='client_secret.json')

open_sheet = c.open('Volunteers form')
wks = open_sheet[0]
cities = set()

i = 2

while wks[i][4]:
    cities.add(wks[i][4])
    i +=1

print(cities)