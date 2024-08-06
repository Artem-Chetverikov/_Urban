class WordsFinder:
    del_char = [',', '.', '=', '!', '?', ';', ':', ' - ', '- ', ' -', '\n']
    all_words = dict()

    def __init__(self, *file_names):
        self.file_names = tuple(file_names)

    def get_all_words(self):
        for name in self.file_names:
            word_lst = []
            with open(name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char_i in self.del_char:
                        line = line.replace(char_i, '')
                    line_word = line.split()
                    word_lst.extend(line_word)
            self.all_words[name] = word_lst
        return self.all_words

    def find(self, word):
        word = word.lower()
        res = dict()
        for name, words in self.get_all_words().items():
            if word in words:
                res[name] = words.index(word) + 1
        return res

    def count(self, word):
        word = word.lower()
        res = dict()
        for name, words in self.get_all_words().items():
            res[name] = words.count(word)
        return res


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))  # 3 слово по счёту
# print(finder2.count('teXT'))  # 4 слова teXT в тексте всего


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))
