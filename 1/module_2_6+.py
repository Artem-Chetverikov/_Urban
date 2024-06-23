def decoder(num):
    password = []
    for i in range(1, num+1):
        for k in range(1, num+1):
            pair = []
            if i == k:
                pair.clear()
                continue
            if num % (i + k) == 0:
                pair.clear()
                pair.append(i)
                pair.append(k)
                pair.sort()
                if pair != [] and pair not in password:
                    password.append(pair)

    password_str = ''
    for i in password:
        for k in i:
            password_str += str(k)

    return password_str


for n in range(3, 21):
    print(f'{n} - {decoder(n)}')
