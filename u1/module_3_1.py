calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    out_lst = list()
    out_lst.append(len(string))
    out_lst.append(string.upper())
    out_lst.append(string.lower())
    return tuple(out_lst)


def is_contains(string: str, list_to_search: list):
    count_calls()
    in_lst_low = []
    for str_i in list_to_search:
        in_lst_low.append(str_i.lower())
    if string.lower() in in_lst_low:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
