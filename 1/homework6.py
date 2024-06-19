my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Vasya'])
print(my_dict.get('Оля'))
my_dict['Петя'] = 2000
my_dict['Саня'] = 2015
delete_name = my_dict.pop('Vasya')
print(my_dict)

my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко'}
print(my_set)
my_set.add(56)
my_set.add('Апельсин')
my_set.remove(42.314)
print(my_set)
