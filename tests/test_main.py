from mi_proyecto.main import saludar

def test_saludar():
    assert saludar("Ana") == "Hola, Ana"