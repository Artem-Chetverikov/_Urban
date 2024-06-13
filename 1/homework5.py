immutable_var = (1, 2, 'a', 'b')
print(immutable_var[0])
#immutable_var[0] = 3    # Ошибка! Кортеж - неизменяемый тип данных
mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[0] = 'Один'
mutable_list[4] = 5
print(mutable_list)
