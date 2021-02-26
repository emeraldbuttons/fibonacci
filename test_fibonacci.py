import unittest
import fibonacci

class TestFibonacciMethods(unittest.TestCase):
    def test_fib(self):
        result = fibonacci.fib(6)
        self.assertEqual(result, [0,1,1,2,3,5])
    def test_factorial(self):
        result = fibonacci.factorial(6)
        self.assertEqual(result, 720)

if __name__ == "__main__":
    unittest.main(verbosity=2)
