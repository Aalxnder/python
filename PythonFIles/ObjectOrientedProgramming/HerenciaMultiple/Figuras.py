class FiguraGeometrica:
    def __init__(self,base,altura):
        self._base = base;
        self._altura = altura;


class Color:
    def __init__(self,color):
        self._color = color;

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,base,color):
        #inicializar los atributos de las clases
        FiguraGeometrica.__init__(self,base,base);
        Color.__init__(self,color);

    def area(self):
        resultado = self._base * self._altura;
        return resultado;

#objetos
lado = float(input("Ingresa un lado del cuadrado: "));
color = input("ingresa el color del cuadrado: ");

cubo = Cuadrado(lado,color);
print(f'Area del cuadrado: {cubo.area()}');
print(Cuadrado.mro());