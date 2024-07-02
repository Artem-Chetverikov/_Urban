def single_root_words(root_word, *other_words):
    same_words = list()
    for word_i in other_words:
        if root_word.lower() in word_i.lower() and not (word_i in same_words):
            same_words.append(word_i)
        if word_i.lower() in root_word.lower() and not (word_i in same_words):
            same_words.append(word_i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Disable', 'Bagel')
print(result1)
print(result2)
