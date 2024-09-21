import threading
from threading import Thread, Lock
from random import randint
from time import sleep


class Bank(Thread):
    lock = Lock()

    def __init__(self):
        super().__init__()
        self.balance = 100
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            with self.lock:
                cash_1 = randint(50, 500)
                self.balance += cash_1
                print(f"Пополнение на: {cash_1}. Текущий баланс{self.balance}")
            if self.balance >= 500 and self.lock.locked():
                 self.lock.release()
                 sleep(0.001)

    def take(self):
        for i in range(100):
            with self.lock:
                cash_2 = randint(50, 500)
                print(f"Запрос на снятие {cash_2}")
                if self.balance >= cash_2:
                    self.balance -= cash_2
                    print(f"Снятие: {cash_2} запрос выполнен. Баланс:{self.balance}")
                else:
                    print(f"Запрос откланён, недостаточно средств")
                    self.lock.acquire()

                sleep(0.001)

bk = Bank()

th1 =threading.Thread(target=Bank.deposit, args=(bk,))
th2 =threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")

