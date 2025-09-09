class Integer:
    @classmethod
    def varify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Кордината должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.varify_coord(value)
        instance.__dict__[self.name] = value

class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



p = Point3D(1,2,3)
print(p.__dict__)

