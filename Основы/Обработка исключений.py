"""
try:
    f = open("testFile.txt")

    f.write("новыйтекст")
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z)
else: ## выполняется если никакое исключение не сработало и программа отработала
    print("Исключений не произошло")
finally:
    f.close()
    print(":")

"""


### Инструкция raise и пользовательские исключения
class ExeptioonPrintSendData(Exception):
    """Класс исключения при отправке данных принтеру"""



class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExeptioonPrintSendData("Принтер не отвечает")

    def send_to_print(self,data):
        return False

p = PrintData()
try:
    p.print("123")
except ExeptioonPrintSendData:
    print("Принтер не хочет отвечать")