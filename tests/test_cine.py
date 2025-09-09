
from Ejercicio1_cine import validar_edad,validar_estudiante
def test_validar_edad():
    assert validar_edad(20) == 20000
    assert validar_edad(10) == 10000
    assert validar_edad(15) == 15000
    assert validar_edad(-8) == "Edad invalida"

def test_validar_estudiante():
  assert validar_estudiante(20000,'si') == 'El costo de su factura con descuento del 10% es de 18000.0'
  assert validar_estudiante(20000,'no') == 'El costo de su entrada es 20000'
  assert validar_estudiante(15000,'si')== 'El costo de su factura con descuento del 10% es de 13500.0'
  assert validar_estudiante(15000,'no') == 'El costo de su entrada es 15000'
  assert validar_estudiante(10000,'si')== 'El costo de su factura con descuento del 10% es de 9000.0'
  assert validar_estudiante(10000,'no') == 'El costo de su entrada es 10000'