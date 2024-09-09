import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        read_str = file.readline()
        while read_str:
            all_data.append(read_str)
            read_str = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    start = datetime.datetime.now()

    # Линейный вызов
    # 0:00:08.858314
    # for file_name in filenames:
    #     read_info(file_name)

    # Многопроцессный
    # 0: 00:04.163778
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    stop = datetime.datetime.now()
    print(stop - start)
