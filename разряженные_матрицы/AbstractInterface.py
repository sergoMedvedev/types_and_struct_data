"""
    Данный класс будет абстрактным для того что бы от него наследвать те методы, которые необходимы
    для того что бы работать с матрицами в данной ЛР.

    - поля

    - методы
    packaging()
    unpackaging()

"""

import abc
class InterfaceForMatrix(abc.ABC):

    #метод, который должен реализовывать упаковку
    @abc.abstractmethod
    def packing(self):
        pass

    #метод, который реализовывает распоковку
    @abc.abstractmethod
    def unpacking(self):
        pass
