# 1. Создать класс TrafficLight (светофор). Определить у него один атрибут color (цвет) и метод running (запуск); атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный); 
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from re import S
from time import sleep

class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("TrafficLight is red now")
            sleep(7)
            print("TrafficLight is yellow now")
            sleep(2)
            print("TrafficLight is green now")
            sleep(7)
            print("TrafficLight is yellow now")
            sleep(2)

trafficLight = TrafficLight()
trafficLight.running()


# 2. Реализовать класс Road (дорога). Определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса; атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна; проверить работу метода.

class Road:
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
               f"{(self._length * self._width * weight * thickness) / 1000} т"

road_1 = Road(5000, 20)
print(road_1.get_full_profit())

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return sum(self._income.values())

manager = Position("Max", "Black", "CEO", 850000, 100000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, 
# что машина поехала, остановилась, повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

from random import choice

class Car:
    direction = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]

    def __init__(self, n, c, s, p = False):
        self.name = n
        self.color = c
        self.speed = S
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a police car? {p}')
    
    def go(self):
        print(f'{self.name}: Car went.')
    
    def stop(self):
        print(f'{self.name}: Car stopped!')
    
    def turn(self):
        print(f'{self.name}: Car turned {choice(self.direction)}.')
    
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'

class TownCar(Car):
    def show_speed(self):
        return f"{self.name}: Car speed: {self.speed}. Speeding!" if self.speed > 60 else super().show_speed()

class WorkCar(Car):
     def show_speed(self):
        return f"{self.name}: Car speed: {self.speed}. Speeding!" if self.speed > 40 else super().show_speed()

class SportCar(Car):
    """ Sports Car"""


class PoliceCar(Car):
    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)

police_car = PoliceCar('"Полицейская"', 'белый', 80)
work_car = WorkCar('"Грузовая"', 'черный', 40)
sport_car = SportCar('"Спортивная"', 'красный', 120)
town_car = TownCar('"Легковая"', 'желтый', 65)

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
    
# 5. Реализовать класс Stationery (канцелярская принадлежность). Jпределить в нём атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title 

    def draw(self):
        print(f"Just start drawing! {self.title}")

class Pen(Stationery):
     def draw(self):
        print(f"Start drawing with {self.title} pen!")

class Pencil(Stationery):
     def draw(self):
        print(f"Start drawing with {self.title} pencil!")

class Marker(Stationery):
     def draw(self):
        print(f"Start drawing with {self.title} marker!")

stat = Stationery()
pen = Pen("Parker")
pencil = Pencil("Faber-Castell")
marker = Marker("COPIC")

office_supplies = [stat, pen, pencil, marker]

for i in office_supplies:
    i.draw()

