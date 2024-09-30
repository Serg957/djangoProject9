import math
class Figure:
    sides_count = 0
    def __init__(self,sides, *color):
        self.set_color(*color)
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.filled = False

    def get_color(self):
        return self.__color
    def set_color(self, r=0, g=0, b=0):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 and isinstance(x, int) for x in [r, g, b])
    def get_sides(self):
        return self.__sides

    def __is_valid_side(self, *new_side):
        return len(new_side) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_side)

    def set_sides(self, *new_side):
        if self.__is_valid_side(*new_side):
            self.__sides = list(new_side)

    def __len__(self):
        return sum(self.__sides)
class Circle(Figure):
    sides_count = 1
    def __init__(self, color, radius):
        super().__init__((radius,), *color)
        self.__radius = self.get_sides()[0] / (2 * math.pi) if self.get_sides()[0] > 0 else 0
    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, *sides, color):
        super().__init__(sides, *color)
        a, b, c = self.get_sides()
        p = (a + b + c)/2
        self.height = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / a if a > 0 else 0
    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.height

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        super().__init__([side] * 12, *color)
        self.__sides = [side] * self.sides_count
    def get_volume(self):
        return self.get_sides()[0] ** 3



#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
#
#
# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216