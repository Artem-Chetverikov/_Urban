
def all_variants(text):
    i = 1
    k = 0
    while i <= len(text):
        while k+i <= len(text):
            str_i = text[k:k+i]
            k = (k + i - 1) if i > 1 else (k + i)
            yield str_i
        i += 1
        k = 0


a = all_variants("abc")
for i in a:
    print(i)
