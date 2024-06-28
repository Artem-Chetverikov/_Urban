def get_multiplied_digits(number: int):
    str_number = str(number)
    if not str_number.isdigit():
        return 0
    str_number = str_number.replace('0', '')
    if len(str_number) == 1:
        return number
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
