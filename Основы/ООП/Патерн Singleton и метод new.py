class DataBase:
    __Instance = None # Задаем пременной значение None

    """
    В методе __new__ перед создаением экземпляра класса, мы проверяем существет ли уже такйо уже
    Если есть то что показывает переменная __Instance то тогда мы не создаем новый экземпляр, 
    в противоположном случае создаем его с помощью записи cls.__Instance = super().__new__(cls)
    csl в здесь указывает не ссылуа на экземпляр класса, а ссылку на сам класс
    
    """

    def __call__(self, *args, **kwargs):
        pass## изучим далее
    def __new__(cls, *args, **kwargs):
        if cls.__Instance is None:
            cls.__Instance = super().__new__(cls)
        return cls.__Instance

    def __del__(self):
        DataBase.__Instance = None


    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print(f"Отключение от базы данных")

    def read(self):
        print(f"Данные из БД")

    def write(self, data):
        print(f"Запись данных в БД: {data}")

user1 = DataBase("Ivanov", 1234, 12)
user2 = DataBase("Glinkov", 532, 10)

print(user1.__dict__)
print(user2.__dict__)