import unittest

class TestMaxProfitFunc(unittest.TestCase):

    def test_max_profit_positive(self):
        # Test case with positive maximum profit
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit_func(prices), 5)

    def test_max_profit_negative(self):
        # Test case with negative maximum profit
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit_func(prices), 0)

    def test_max_profit_zero(self):
        # Test case with maximum profit as zero
        prices = [2, 2, 2, 2, 2]
        self.assertEqual(max_profit_func(prices), 0)

    def test_max_profit_single_element(self):
        # Test case with a single element list
        prices = [5]
        self.assertEqual(max_profit_func(prices), 0)

    def test_max_profit_empty_list(self):
        # Test case with an empty list
        prices = []
        self.assertEqual(max_profit_func(prices), 0)

if __name__ == '__main__':
    unittest.main()
