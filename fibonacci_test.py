import pytest
import fibonacci

class TestClass:
    def test_fib(self):
        result = fibonacci.fib(6)
        assert result == [0,1,1,2,3,5]

    def test_factorial(self):
        result = fibonacci.factorial(6)
        assert result == 720
