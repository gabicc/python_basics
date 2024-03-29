import basic_classes

v = basic_classes.Volei(60, 3.14, ['Ion', 'Gigel', 'Andrei', 'Ianis', 'Radu', 'Tudor'])

v.show_arrangement()
print('---------------')

v.rotate()

t = basic_classes.Tenis_de_masa(30, 5.4, 3)

print(t.get_max_sets())