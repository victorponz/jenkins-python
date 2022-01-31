import unittest
from calculadora import Calculadora 
class TestSum(unittest.TestCase):
    
    def test_sum(self):
        c = Calculadora()
        self.assertEqual(c.multiplicar(1, 2), 2, "Should be 2")

if __name__ == '__main__':
    unittest.main()