class Pc():
    def turn_on(self):
        print("Вы нажали на кнопку")
        self.__pit()
        self.__press_exit()
        self._turn_off()

    def __pit(self):
        print("подача питания на пк и включение")

    def __press_exit(self):
        print("вы нажали на кнопку выключние")

    def _turn_off(self):
        print("Выключение")

my_pc = Pc()
my_pc.turn_on()
