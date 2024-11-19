import unittest
from unittest import *


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

        # отсортируем бегунов по их скорости, чтобы бегун с большей
        # скоростью всегда приходил первым:
        self.participants.sort(key=lambda c: c.speed, reverse=True)

    def start(self):
        finishers = {}
        place = 1
        while sum([run_i.speed for run_i in self.participants if run_i is not None]):
            for participant in enumerate(self.participants, 0):
                if participant[1] is None:
                    continue
                participant[1].run()
                if participant[1].distance >= self.full_distance:
                    finishers[place] = participant[1].name
                    place += 1
                    self.participants[participant[0]] = None

        return finishers



class RunnerTest(TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run_1 = Runner("Бегун №1")
        for _ in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_1 = Runner("Бегун №1")
        for _ in range(10):
            run_1.run()
        self.assertEqual(run_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_1 = Runner("Бегун №1")
        run_2 = Runner("Бегун №2")

        for _ in range(10):
            run_1.run()
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)


class TournamentTest(TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run_1 = Runner('Усэйн', 11)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_01(self):
        tour = Tournament(90, self.run_1, self.run_3)
        self.all_results.append(tour.start())
        max_key = max(key_i for key_i, val_i in self.all_results[-1].items())
        self.assertTrue(self.all_results[-1][max_key] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_02(self):
        tour = Tournament(90, self.run_2, self.run_3)
        self.all_results.append(tour.start())
        max_key = max(key_i for key_i, item_i in self.all_results[-1].items())
        self.assertTrue(self.all_results[-1][max_key] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_03(self):
        tour = Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_results.append(tour.start())
        max_key = max(key_i for key_i, item_i in self.all_results[-1].items())
        self.assertTrue(self.all_results[-1][max_key] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_04(self):
        tour = Tournament(1, self.run_3, self.run_2, self.run_1)
        self.all_results.append(tour.start())
        max_key = max(key_i for key_i, item_i in self.all_results[-1].items())
        self.assertTrue(self.all_results[-1][max_key] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        print()
        for res in cls.all_results:
            print(res)
