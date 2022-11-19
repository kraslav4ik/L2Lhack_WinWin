import pygsheets

c = pygsheets.authorize(client_secret='client_secret.json')

open_sheet = c.open('Volunteers form')
wks = open_sheet[0]
cities = set()
helps = set()

LIFE = 'Рассказать, как в вашей стране решаются бытовые вопросы — поиск работы, жилья, открытие счета и т.д.'
LEGAL = 'Рассказать про способы эмиграции в вашу страну и легализации в ней'
JOB = 'Проконсультировать по вашей специализации (как врач, юрист,  IT-специалист и т.д)'
BED = 'Предоставить спальное место эмигранту на короткий срок'
CHAT = 'Присоединиться к чату «Ковчега» по вашей стране и в свободное время отвечать на вопросы'
GUIDE = 'Составить гайд или провести вебинар по близкой вам теме (Например: «Переезд в ЕС по по Голубой карте», «Возможности для эмигрантов в Канаде» и т.д)'
LEARN = 'Научить эмигрантов чему-то (основы иностранного языка, как пользоваться криптовалютами и т.д)'
EXPERIENCE = 'Рассказать про ваш опыт эмиграции в канале «Ковчега»'
WORK = 'Предложить эмигрантам вакансию с удаленкой и/или релокацией'
DONAT = 'Помочь проекту финансово (подробности на сайте antiwarcommittee.info/kovcheg)'
PSYCHO = 'Я психолог и могу оказывать пострадавшим бесплатные консультации'

i = 2

while wks[i][4]:
    cities.add(wks[i][4])
    i +=1


print(cities)