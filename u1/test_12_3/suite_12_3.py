import test_12_3
import unittest

run_TS = unittest.TestSuite()
run_TS.addTests(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
run_TS.addTests(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_TS)
