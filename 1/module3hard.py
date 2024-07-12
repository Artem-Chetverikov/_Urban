import numbers

sum_all = 0


def calculate_structure_sum(*args):
    global sum_all
    for item in args:
        if isinstance(item, bool):
            sum_all = sum_all+len(str(item))
        if isinstance(item, str):
            sum_all = sum_all+len(item)
        if isinstance(item, numbers.Number):
            sum_all = sum_all+item
        if isinstance(item, list):
            for item_i in item:
                calculate_structure_sum(item_i)
        if isinstance(item, tuple):
            for item_i in item:
                calculate_structure_sum(item_i)
        if isinstance(item, set):
            for item_i in item:
                calculate_structure_sum(item_i)
        if isinstance(item, dict):
            for item_i, item_k in item.items():
                calculate_structure_sum(item_i)
                calculate_structure_sum(item_k)
    return sum_all


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
