class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название : {self.name}, количество этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        new_floor += 1

        for i in range(1, new_floor):
            if 1 <= new_floor <= (self.number_of_floors + 1):
                print(i)
            else:
                print('Такого этажа нет')
                return


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))
