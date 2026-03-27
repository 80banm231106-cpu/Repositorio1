from app import multiplicacion

def test_multiplicacion():
    assert multiplicacion(7, 4) == 28

def test_multiplicacion_2():
    assert multiplicacion(9, 9) == 81