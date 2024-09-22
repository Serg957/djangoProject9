import time
from threading import Thread
import queue
from random import randint
class Table():
    def __init__(self,number,guest=None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        servised_time = randint(3,10)
        time.sleep(servised_time)



class Cafe:
    def __init__(self,*args):
        global queue
        self.queue = queue.Queue()
        self.tables = args


    def guest_arrival(self,*guest):
        servis = list()
        for i in guest:
            for j in self.tables:
                if j.guest == None:
                    servis.append(i)
                    j.guest = i
                    print(f'{i.name} сел(-а) за стол номер {j.number}')
                    break
            if (i in servis) == False:
                self.queue.put(i)
                print(f'{i.name} в очереди')
        for i in servis: i.start()


    def discuss_guests(self):
        free_tables = 0
        while True:
            for i in self.tables:
                if (i.guest.is_alive()==False) or (self.queue.empty()):
                    print(f'{i.guest.name} за текущим столом> покушал(-а) и ушёл(ушла)\nСтол номер {i.number} свободен')
                    i.guest.join()
                    i.guest = None
                if (self.queue.empty() == False) and (i.guest == None):
                    i.guest = self.queue.get()
                    print(f'{i.guest.name} вышел(-ла) из очереди'
                              f' и сел(-а) за стол номер {i.number}')
                    i.guest.start()
                elif i.guest == None:
                    free_tables +=1
                    if free_tables == len(self.tables):
                        return



tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()