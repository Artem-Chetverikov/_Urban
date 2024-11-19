def custom_write(file_name, strings):
    strings_positions = dict()
    strings = enumerate(strings, 1)
    file = open(file_name, 'w', encoding='utf-8')
    for num_i, str_i in strings:
        key_str = tuple([num_i, file.tell()])
        file.write(str_i + '\n')
        strings_positions[key_str] = str_i
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
