import sys


class ErrorEntity:
    """
    класс ошибок для ОПЗ(ОК)
    """
    def __init__(self):
        self.name=None


    def error_OPZ_undefind_arg(self):
        print("Не было нейдено 2 рагумента. Fatal!")
        sys.exit()

    def error_OPZ_ziro_in_otr_stepene(self):
        print("Нуль в отричательной степени. деление на нуль")
        sys.exit()
