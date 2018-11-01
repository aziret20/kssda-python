class Character:
    name = ''  # имя
    type = None  # type
    health = 50  # здоровье
    speed = 50  # скорость
    strength = 50  # сила

    def __init__(self, name=None):

        if name is not None:
            self.name = name
