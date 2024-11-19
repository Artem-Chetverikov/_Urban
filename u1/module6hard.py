import math


class Figure:
    filled = False

    def __init__(self, color, *sides, sides_count=0):
        self.__sides = []
        self.sides_count = sides_count
        self.__color = list(color)
        if len(sides) == sides_count:
            self.__sides = list(sides)
        else:
            for i in range(0, sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *color):
        for part in color:
            if not isinstance(part, int):
                return False
            if part not in range(0, 256):
                return False
        return True

    def set_color(self, *color):
        if len(color) != 3:
            return
        if self.__is_valid_color(*color):
            self.__color = list(color)

    def __is_valid_sides(self, *sides):
        sides = list(sides)
        for side_i in sides:
            if not isinstance(side_i, int):
                return False
            if side_i <= 0:
                return False
        if len(sides) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides, sides_count=1)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides, sides_count=3)
        self.__height = self.get_sides()[0] * (3 ** 0.5) / 2

    def get_square(self):
        perim_tr = sum(self.get_sides()) / 2
        square_tr = (perim_tr * (perim_tr - self.get_sides()[0]) * (perim_tr - self.get_sides()[1]) * (
                perim_tr - self.get_sides()[2])) ** 0.5
        return square_tr


class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides, sides_count=12)
        if len(sides) > 1:
            self.__sides = [1 for i in range(0, 12)]
        else:
            self.__sides = [sides[0] for i in range(0, 12)]
        self.__height = self.get_sides()[0] * (3 ** 0.5) / 2

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            if self.__is_valid_sides(*new_sides):
                self.__sides = [new_sides[0] for i in range(0, 12)]
        else:
            return

    def get_sides(self):
        return self.__sides


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# и площадь:
print(circle1.get_square())

# Проверка объёма (куба):
print(cube1.get_volume())


c1 = Circle((200, 200, 100), 10, 15, 6)
t1 = Triangle((200, 200, 100), 10, 6)
cu1 = Cube((200, 200, 100), 9)
cu2 = Cube((200, 200, 100), 9, 12)

print(c1.get_sides())
print(t1.get_sides())
print(cu1.get_sides())
print(cu2.get_sides())

t2 = Triangle((200, 200, 100), 10, 6, 5)
print(t2.get_square())
