friends = ['дмитро', 'анастасія', 'сашко']
friends[2] = 'данило'
friends.insert(0, 'іван')
friends.insert(2, 'владислав')
friends.append('аліна')
notif = "Мені дуже не зручно, але на вечерю будуть запрошені лише двоє... "
print(notif)
print('\n')
notif_2 = "Вибач, "
notif_3 = ", але я змушений скасувати твоє запрошення. Вибач за незручності."
person = friends.pop()
print(notif_2 + person.title() + notif_3)
person_1 = friends.pop()
print(notif_2 + person_1.title() + notif_3)
person_2 = friends.pop()
print(notif_2 + person_2.title() + notif_3)
person_3 = friends.pop()
print(notif_2 + person_3.title() + notif_3)
print('\n')
notif_4 = ", наша вечірка в силі. чекаю на зустріч!"
print(friends[0].title() + notif_4)
print(friends[1].title() + notif_4)
del friends[0]
del friends[0]
print(friends)
