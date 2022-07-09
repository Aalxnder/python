#Calcular el area de un rectangulo

class Rectangulo:
    def __init__(this, base, altura):
        this.base = base;
        this.altura = altura;

    def area(this):
        return this.base * this.altura;

    def perimetro(this):
        return (this.base+this.altura)*2;

base = float(input("Ingresa la base:\n"));
altura = float(input("Ingresa la altura:\n"));

rectangulo = Rectangulo(base,altura);
print(f'Base: {rectangulo.area():.2f} altura: {rectangulo.perimetro():.2f}');

