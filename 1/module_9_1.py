
def apply_all_func(int_list, *functions):
    results = dict()
    for func_i in functions:
        results[func_i.__name__] = func_i(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
