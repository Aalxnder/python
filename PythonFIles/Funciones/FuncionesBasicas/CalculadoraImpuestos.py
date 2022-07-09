# ejercicio calculadora de impuestos
# crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado
# formula: pago total = pago sin impuestos + pago sin impuestos*(impuesto/100);

def calcularimpuestos(pagoSinImpuestos, montoImpuestos):
    pagoTotal = pagoSinImpuestos+pagoSinImpuestos*(montoImpuestos/100)
    return pagoTotal

pago = float(input("Ingresa el pago sin impuestos:\n"))
impuesto = float(input("Ingresa la taza de impuestos:\n"))

PagoTotal = calcularimpuestos(pago, impuesto)
print(f'El pago total con impuestos es {PagoTotal}')
