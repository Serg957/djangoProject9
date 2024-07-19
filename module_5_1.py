class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor += 1

        for i in range(1, new_floor):
            if 1 <= new_floor <= (self.number_of_floors + 1):
                print(i)
            else:
                print('Такого этажа нет')
                return


h1 = House('ЖК Эльбрус', 30)
h1.go_to(5)
h1.go_to(31)
