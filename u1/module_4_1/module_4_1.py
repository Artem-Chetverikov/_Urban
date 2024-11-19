from fake_math import divide as divide_0
from true_math import divide as divide_inf

result1 = divide_0(69, 3)
result2 = divide_0(3, 0)
result3 = divide_inf(49, 7)
result4 = divide_inf(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
