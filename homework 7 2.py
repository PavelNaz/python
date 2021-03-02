from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, data):
        self.data = data

    @property
    def overall_consumption(self):
        return f'Сумма затраченной ткани равна:{self.data / 6.5 + 0.5 + 2 * self.data + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Abstract meaning'


class Coat(Clothes):
    def consumption(self):
       return f'Сумма ткани для пальто {self.data / 6.5 + 0.5:.2f}'

    def abstract(self):
        return 'First abstract meaning'

class Suit(Clothes):
    def consumption(self):
        return f'Сумма ткани для костюма {2 * self.data + 0.3:.2f}'

    def abstract(self):
        return 'Second abstract meaning'

coat = Coat(400)
suit = Suit(45)
print(coat.consumption())
print(suit.consumption())
print(coat.abstract())
print(suit.abstract())

