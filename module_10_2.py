from threading import Thread    # Импортируем из модуля многопоточности threading класс Thread
from time import sleep          # Импортируем sleep из модуля time для создания задержки

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100                 # Враг по условию задания

    def run(self):
        print(f"{self.name}, на нас напали!")      # В начале битвы выводим сообщение в консоль
        i = 0                                      # Дни битвы
        while self.enemy > 0:                      # Цикл. Пока количество солдат больше нуля
            i += 1                                 # Считаем дни битвы
            self.enemy = self.enemy - self.power   # Каждый день количество врагов уменьшается на power текущего рыцыря
            print(f"{self.name}, сражается {i} день (дня), осталось {self.enemy} воинов.")  # По прошествию 1 дня сражения
                                                                                 # (1 секунды) выводим строку в консоль
            sleep(1)                              # Задержка 1 сек
            if self.enemy == 0:
                print(f"{self.name} одержал победу спустя {i} дней(дня)!")  # Когда враги закончились, выводим строку
                                                                            # в консоль

first_knight = Knight('Sir Lancelot', 10)  # Создание первого потока
second_knight = Knight("Sir Galahad", 20)  # Создание второго потока

#--------------  При старте метод start проверяет был ли вызван метод __init__ у класса Knight  -----------

first_knight.start()   #  Запуск первого потока.
second_knight.start()  #  Запуск второго потока

first_knight.join()   #  Ожидаем завершения первого потока
second_knight.join()  #  Ожидаем завершения второго потока

print("Все битвы закончились!")   # По завершению работы потоков выводим строку в консоль
