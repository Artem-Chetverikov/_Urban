from unittest import *


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):

    def test_walk(self):
        run_1 = Runner("Бегун №1")
        for _ in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    def test_run(self):
        run_1 = Runner("Бегун №1")
        for _ in range(10):
            run_1.run()
        self.assertEqual(run_1.distance, 100)

    def test_challenge(self):
        run_1 = Runner("Бегун №1")
        run_2 = Runner("Бегун №2")

        for _ in range(10):
            run_1.run()
            run_1.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)
