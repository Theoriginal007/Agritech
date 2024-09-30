import unittest

class TestModule1(unittest.TestCase):
    
    def test_addition(self):
        result = 1 + 1
        self.assertEqual(result, 2)

    def test_subtraction(self):
        result = 5 - 3
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
