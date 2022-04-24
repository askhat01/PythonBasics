# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные 
# (список списков) для формирования матрицы. Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.

a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))
    
    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
            return '\n'.join(map(str, c))

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"Matrix 1 + matrix_2\n{matrix_1 + matrix_2}")

# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, 
# которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют 
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
# Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом 
# уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param
    
    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"

class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5
    
class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)
    
coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)

# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его конструкторе 
# инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки 
# арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы 
# должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление 
# клеток, соответственно. В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell:
    def __init__(self, nums):
        self.nums = nums #13
    
    def make_order(self, rows): #5
        return '\n'.join(['Символ_1' * rows for _ in range(self.nums // rows)]) + '\n' + 'Символ_2' * (self.nums % rows)
    
    def __str__(self):
        return f"{self.nums}"
    
    def __add__(self, other):
        print("Sum of cell is:")
        return Cell(self.nums + other.nums)
    
    def __sub__(self, other):
        print("Subtraction of cell is:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше второй, вычитание невозможно!"
    
    def __mul__(self, other):
        print("Multiply of cell is:")
        return Cell(self.nums * other.nums)
    
    def __floordiv__(self, other):
        print("Truediv of cell is:")
        return Cell(self.nums // other.nums)

cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))

    