import logging
from unittest import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler("runner_tests.log", mode='w', encoding='UTF-8')
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


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

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(TestCase):

    def test_walk(self):
        try:
            run_1 = Runner("Бегун №1", -5)
            for _ in range(10):
                run_1.walk()
            self.assertEqual(run_1.distance, 50)
            logger.info('"test_walk" выполнен успешно')
        except ValueError:
            logger.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run_1 = Runner(2, 5)
            for _ in range(10):
                run_1.run()
            self.assertEqual(run_1.distance, 100)
            logger.info('"test_run" выполнен успешно')
        except TypeError:
            logger.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        run_1 = Runner("Бегун №1")
        run_2 = Runner("Бегун №2")

        for _ in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)
