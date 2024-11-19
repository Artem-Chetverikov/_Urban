import datetime
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as file_curr:
        for i in range(1, word_count):
            file_curr.write(f"Какое-то слово №{i}")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


start_t = datetime.datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

stop_t = datetime.datetime.now()
print(f'Работа потоков {stop_t - start_t}')

start_t = datetime.datetime.now()

tr1 = Thread(target=write_words, args=(10, 'example5.txt'))
tr2 = Thread(target=write_words, args=(30, 'example6.txt'))
tr3 = Thread(target=write_words, args=(200, 'example7.txt'))
tr4 = Thread(target=write_words, args=(100, 'example8.txt'))

tr1.start()
tr2.start()
tr3.start()
tr4.start()

tr1.join()
tr2.join()
tr3.join()
tr4.join()

stop_t = datetime.datetime.now()
print(f'Работа потоков {stop_t - start_t}')
