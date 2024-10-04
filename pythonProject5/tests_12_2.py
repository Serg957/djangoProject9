import runner_and_tournament as ran
import unittest



class Tournament_test(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.r1 = ran.Runner('Усэйн', 10)
        self.r2 = ran.Runner('Андрей', 9)
        self.r3 = ran.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)


    def test_challenge_1(self):
        self.tour = ran.Tournament(90, self.r1, self.r3)
        test_1 = self.tour.start()
        Tournament_test.all_results['test_1'] = test_1
        self.assertTrue(test_1[max(test_1.keys())] == 'Ник')

    def test_challenge_2(self):
        self.tour = ran.Tournament(90, self.r2, self.r3)
        test_2 = self.tour.start()
        Tournament_test.all_results['test_2'] = test_2
        self.assertTrue(test_2[max(test_2.keys())] == 'Ник')

    def test_challenge_3(self):
        self.tour = ran.Tournament(90, self.r1, self.r2, self.r3)
        test_3 = self.tour.start()
        Tournament_test.all_results['test_3'] = test_3
        self.assertTrue(test_3[max(test_3.keys())] == 'Ник')



if __name__ == '__main__':
    unittest.main()




