import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        walker = runner.Runner("walker")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner_1 = runner.Runner("runner_1")
        for i in range(10):
            runner_1.run()
        self.assertEqual(runner_1.distance, 100)



    def test_challenge(self):

        runner_r = runner.Runner("runner_r")
        runner_w = runner.Runner("runner_w")
        for i in range(10):
            runner_r .run()
            runner_w.walk()

        self.assertNotEqual(runner_r.distance, runner_w.distance)



if __name__ == '__main__':
    unittest.main()
