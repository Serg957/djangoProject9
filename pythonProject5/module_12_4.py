import unittest
import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        try:
            walk1 = Runner('First', -5)
            for i in range(10):
                walk1.walk()
            self.assertEqual(walk1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.exception('Неверная скорость для Runner')
            raise

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        try:
            walk2 = Runner(234)
            for j in range(10):
                walk2.run()
            self.assertEqual(walk2.distance, 100)
            logging.info('"test_run" успешно выполнен')
        except TypeError:
            logging.exception('Неверный тип данных для объекта Runner')
            raise

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        walk3 = Runner('Third')
        walk4 = Runner('Fourth')
        for k in range(10):
            walk3.run()
            walk4.walk()
        self.assertNotEqual(walk3.distance, walk4.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format="%(asctime)s | %(levelname)s : %(message)s")
