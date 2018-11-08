from lesson_4.base import Character, Medic


class Wizard(Character, Medic):
    type = 'wizard'

    def greet(self):
        return 'Youhoo my name is {} and i am {}'.format(self.name, self.type)
