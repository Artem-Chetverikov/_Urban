import datetime
from time import sleep
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        self.enemy_cnt = 100
        self.name_r = name
        self.power = power
        super().__init__()

    def run(self):
        print(f"{self.name_r}, на нас напали!")
        time_cnt = 0
        while self.enemy_cnt > 0:
            self.enemy_cnt -= self.power
            sleep(1)
            time_cnt += 1
            if self.enemy_cnt > 0:
                print(f"{self.name_r} сражается {time_cnt} день(дня)..., осталось {self.enemy_cnt} воинов.")
            else:
                print(f"{self.name_r} одержал победу спустя {time_cnt} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
