import unittest

class TestModule2(unittest.TestCase):
    
    def test_multiplication(self):
        result = 2 * 3
        self.assertEqual(result, 6)

    def test_division(self):
        result = 10 / 2
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
