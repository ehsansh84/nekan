class consts(object):
    import os
    PROJECT_NAME = 'nekan'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    page_size = 20
    MAX_TOKEN_DURATION = 1000000
    MESSAGES = None
    NOTIFICATIONS = None
    CONSOLE_LOG = True
    LOG_ACTIVE = True
    PDP_ROOT = '/www/'
    CDN_ADDRESS = 'https://cdn.domain.info'
    ODP_ROOT = CDN_ADDRESS + '/'+ PROJECT_NAME +'/'
    PDP_IMAGES = PDP_ROOT + 'images/'
    SERVER_PORT = '8282'
    DB_NAME = PROJECT_NAME
    ODP_IMAGES = ODP_ROOT + 'images/'
    TEST_MODE = False






class Car:
    """
    Setup the default state of car object
    """

    def __init__(self):
        self.speed = 0              # default speed
        self.MAX = 120              # max speed
        self.BREAK_AMOUNT = 10      # break amount in mph
        self.color_options = {      # color options for the car
            1: 'black',
            2: 'green',
            3: 'orange',
            4: 'white',
            5: 'pink'
        }

        self.current_color = self.color_options[1]

    def __repr__(self):
        """
        Create a string representation of car object
        :return: current speed and color
        """
        return f'Speed: {self.speed} Color: {self.current_color}'

    def change_color(self, option) -> int:
        """
        changes color of car, choose values 1-5
        :param option: the new color of the car
        :return: the current color of car
        """
        try:
            if 1 <= option <= 5:
                if self.current_color == self.color_options[option]:
                    return self.current_color
                else:
                    self.current_color = self.color_options[option]
                    return self.current_color
        except TypeError:
            print('Ints: 1-5')

    def accelerate(self, velocity, max=120) -> int:
        """
        increase speed of car
        :param velocity: speed up amount
        :param max: limit to speed increase
        :return:  current speed
        """
        try:
            if self.speed < self.MAX and velocity > 0:
                self.speed += velocity
        except ValueError:
            print(f'self.speed or velocity are invalid. Your values: {velocity}, or {self.speed}')
        return self.speed

    def brake(self, velocity) -> int:
        """
        decelerate your car
        :param velocity: rate of slow down
        :return: current speed
        """
        try:
            if self.speed - velocity < 0 or velocity > self.BREAK_AMOUNT:
                raise ValueError
            else:
                self.speed -= velocity
                return self.speed
        except ValueError:
            print('invalid')


import unittest


class TestCar(unittest.TestCase):

    def test_default_color(self):
        self.c1 = Car()
        self.assertEqual(self.c1, 'orange')

    def test_change_color(self):
        self.c1 = Car()
        self.assertEqual(self.c1.change_color(3), 'blue')

    def test_current_speed(self):
        self.c1 = Car()
        self.assertEqual(self.speed, 0)

    def test_accelerate(self):
        self.c1 = Car()
        self.c1.accelerate(10)
        self.c1.accelerate(20)
        self.c1.accelerate(100)
        self.assertEqual(self.c1.speed, 20)

    def test_brake(self):
        self.c1 = Car()
        self.c1.brake(5)
        self.assertEqual(self.c1.speed, 5)


if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
