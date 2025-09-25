import unittest
import my_utils


class TestMyUtilFactorial(unittest.TestCase):

    def test_factorial_of_valid_input(self):
        expected = 120
        actual = my_utils.factorial(5)
        self.assertEqual(expected, actual)

    def test_factorial_of_zero(self):
        want = 1
        got = my_utils.factorial(0)
        self.assertEqual(want, got)

    def test_factorial_of_str(self):
        with self.assertRaises(TypeError):
            my_utils.factorial("ten")
            
    def test_factorial_of_negative_input(self):
        def f():
            my_utils.factorial(-5)
        self.assertRaises(ValueError, f)

    def test_factorial_of_negative(self):
        try:
            my_utils.factorial(-5)
            self.fail('expected ValueError, did not get one.')
        except ValueError:
            ...

    def test_factorial_of_multiple_valid_inputs(self):
        test_cases = [
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
            (7, 5040),
            (8, 40320),
        ]
        for num, expected in test_cases:
            with self.subTest():
                actual = my_utils.factorial(num)
                self.assertEqual(expected, actual)



# python -m unittest ex32_unit_test_demo.py
# python ex32_unit_test_demo.py
if __name__ == '__main__':
    unittest.main()
