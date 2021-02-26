import unittest
import fibonacci

class TestFibonacciMethods(unittest.TestCase):
    def test_fib(self):
        result = fibonacci.fib(6)
        self.assertEqual(result, [0,1,1,2,3,5])

if __name__ == "__main__":
    unittest.main(verbosity=2)
