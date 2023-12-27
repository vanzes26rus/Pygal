from random import randint
class Dia():
    def __init__(self, num_saids=6):
        """Класс представляющий кубик"""
        self.num_saids = num_saids

    def rool(self):
        """Возвращает значение от 1 до 2"""
        return randint(1, self.num_saids)