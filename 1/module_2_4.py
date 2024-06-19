numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for item in numbers:
    if item <= 1:
        continue

    is_prime = True
    i = 2
    while i < item:
        if item % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        primes.append(item)
    else:
        not_primes.append(item)

print(not_primes)
print(primes)
