from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest_i in guests:
            table_free = None
            for tab_i in self.tables:
                if tab_i.guest is None:
                    table_free = tab_i
                    break
            if table_free is not None:
                table_free.guest = guest_i
                guest_i.start()
                print(f"{guest_i.name} сел(-а) за стол номер {table_free.number}")
            else:
                self.queue.put(guest_i)
                print(f"{guest_i.name} в очереди")

    def discuss_guests(self):
        table_occupied = None
        for tab_i in self.tables:
            if tab_i.guest is not None:
                table_occupied = tab_i

        while table_occupied is not None:
            for tab_i in self.tables:
                if tab_i.guest is not None:
                    if not tab_i.guest.is_alive():
                        print(f"{tab_i.guest.name} покушал(-а) и ушёл(ушла)")
                        tab_i.guest = None
                        print(f"Стол номер {tab_i.number} свободен")

            if not self.queue.empty():
                table_free = None
                for tab_i in self.tables:
                    if tab_i.guest is None:
                        table_free = tab_i
                        break
                if table_free is not None:
                    table_free.guest = self.queue.get()
                    table_free.guest.start()
                    print(
                        f"{table_free.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table_free.number}")
            table_occupied = None
            for tab_i in self.tables:
                if tab_i.guest is not None:
                    table_occupied = tab_i


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
