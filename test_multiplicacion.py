import unittest
from app import multiplicacion  

class TestMultiplicacion(unittest.TestCase):

    def test_multiplicar(self):
        self.assertEqual(multiplicacion(7,4), 28)

if __name__ == "__main__":
    unittest.main()