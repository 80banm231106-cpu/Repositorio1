import unittest
from test_app import multiplicacion  # o el nombre de tu archivo

class TestMultiplicacion(unittest.TestCase):

    def test_multiplicar(self):
        self.assertEqual(multiplicacion(7,4), 28)

if __name__ == "__ain__":
    unittest.main()