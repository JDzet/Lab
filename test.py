""""
class Transport:
    "Создание класса"
    def __init__(self, brand, max_speed):
        self._brand = brand # _ перед brand ограничивает для пользователей доступ к этому атрибуту __полный запрет
        self.max_speed = max_speed
        self.on()

    def on(self):

        print("Это класс транспорт")


class Car(Transport):
    def __init__(self,brand, max_speed, num_doors):
        super().__init__(brand, max_speed)
        self.num_doors = num_doors

    def car_info(self):
        return f"Марка: {self._brand}, Макс. скорость: {self.max_speed}, Дверей: {self.num_doors}"

my_car = Car("Toyota", 200, 4)
"""


class Goods:
    def __init__(self, name, weight, price):
        print("init MixingLog")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


