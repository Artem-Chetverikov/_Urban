
def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        # Проверяем число простое/сложное
        prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
        i = 5
        d = 2
        while prime and i * i <= num:
            prime = num % i != 0
            i += d
            d = 6 - d
        if prime:
            print('Простое')
        else:
            print('Сложное')
        return num
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
