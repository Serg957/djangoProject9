import runner_and_tournament as rat
import unittest, runner


class TournamentError(Exception):
    pass

is_frozen= False

class RunnerTest(unittest.TestCase):
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = runner.Runner("walker")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_1 = runner.Runner("runner_1")
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        runner_r =runner. Runner("runner_r")
        runner_w = runner.Runner("runner_w")
        for i in range(10):
            runner_r .run()
            runner_w.walk()

        self.assertNotEqual(runner_r.distance, runner_w.distance)


class Tournament_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.is_frozen = True
    def setUp(self):
        self.r1 = rat.Runner('Усэйн', 10)
        self.r2 = rat.Runner('Андрей', 9)
        self.r3 = rat.Runner('Ник', 3)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_1(self):
        self.tour = rat.Tournament(90, self.r1, self.r3)
        test_1 = self.tour.start()
        Tournament_test.all_results['test_1'] = test_1
        self.assertTrue(test_1[max(test_1.keys())] == 'Ник')

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_2(self):
        self.tour = rat.Tournament(90, self.r2, self.r3)
        test_2 = self.tour.start()
        Tournament_test.all_results['test_2'] = test_2
        self.assertTrue(test_2[max(test_2.keys())] == 'Ник')

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge_3(self):
        self.tour = rat.Tournament(81, self.r1, self.r2, self.r3)
        test_3 = self.tour.start()
        Tournament_test.all_results['test_3'] = test_3
        self.assertTrue(test_3[max(test_3.keys())] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)


if __name__ == '__main__':
    unittest.main()