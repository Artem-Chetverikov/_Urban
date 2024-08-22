
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num_i in numbers:
        try:
            result += num_i
        except TypeError:
            print('Некорректный тип данных для подсчёта суммы -', num_i)
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_num, cnt_not_num = personal_sum(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

    cnt_num = len(numbers) - cnt_not_num
    avr = 0
    try:
        avr = sum_num / cnt_num
    except ZeroDivisionError:
        avr = 0
    finally:
        return avr


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
