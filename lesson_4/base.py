# создать персонажа
# задать имя
# определить свойтсва

class Medic:
    def heal(self):
        self.health = 100

class Character:
    name = ''  # имя
    type = None  # type
    health = 50  # здоровье
    speed = 50  # скорость
    strength = 5  # сила
    level = 1  # уровень

    def __init__(self, name=None, level=None):
        if name is not None:
            self.name = name

        if level is not None:
            self.level = level

    def greet(self):
        return 'Hello my name is {} and i am {}'.format(self.name, self.type)

    def punch(self):
        return self.strength * self.level

    def heal(self):
        self.health = 70
