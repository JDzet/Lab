class Transport:

    def __init__(self, brand, max_speed):
        self._brand = brand # _ перед brand ограничивает для пользователей доступ к этому атрибуту __полный запрет
        self.max_speed = max_speed



class Car(Transport):
    def __init__(self,brand, max_speed, num_doors):
        super().__init__(brand, max_speed)
        self.num_doors = num_doors

    def car_info(self):
        return f"Марка: {self._brand}, Макс. скорость: {self.max_speed}, Дверей: {self.num_doors}"

my_car = Car("Toyota", 200, 4)

print(my_car.car_info())

print(my_car.__dict__) # выводит данные пространства имен экземпляра класса