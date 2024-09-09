from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            plus_bal = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += plus_bal
            print(f"Пополнение: {plus_bal}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for _ in range(100):
            minus_bal = randint(50, 500)
            print(f"Запрос на {minus_bal}")

            if self.balance >= minus_bal:
                self.balance -= minus_bal
                print(f"Снятие: {minus_bal}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
