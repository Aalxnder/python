# tener una clase llamada FiguraGeometrica, en la cual sus atributos estaran encapsulados
# con los siguientes datos:
# -Atributos = alto,ancho
# -metodos = getters y setters de los atributos
#
# se debera tener otra clase padre llamada Color igual encapsulada con los siguientes datos:
# -atributos: color
# -metodos : setter y getter del atributos
#
# y dos clases hijas llamadas , cuadrado y rectangulo con los siguientes datos
# -metodos Area(), __str__().

#clases padre
class FiguraGeometrica:
    def __init__(self,ancho,alto):
        if(self._validarValor(ancho)):
            self._ancho = ancho;
        else:
            self._ancho = 0;
            print(f'Valor erroneo {ancho}');
        if(self._validarValor(alto)):
            self._alto = alto;
        else:
            self._alto = 0;
            print(f'Valor Erroneo {alto}');

    #setter y getters
    @property
    def ancho(self):
        return self._ancho;

    @ancho.setter
    def ancho(self,ancho):
        if (self._validarValor(ancho)):
            self._ancho = ancho;
        else:
            self._ancho = 0;
            print(f'Valor Erroneo {ancho}');

    @property
    def alto(self):
        return self._alto;

    @alto.setter
    def alto(self, alto):
        if(self._validarValor(alto)):
            self._alto = alto;
        else:
            print(f'Valor erroneo {alto}');
            self._alto = 0;
    #metodo __Str__()
    def __str__(self):
        return f'Datos de la figura:\nAlto: {self._alto},Ancho: {self.ancho}';

    def _validarValor(self,valor):
        return True if 0<valor<100 else False;
class Color:
    def __init__(self,color):
        self._color = color;

    @property
    def color(self):
        return self._color;
    @color.setter
    def color(self,color):
        self._color = color;

    def __str__(self):
        return f'Color: {self._color}';

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado);
        Color.__init__(self,color);

    def CalcularArea(self):
        return self.alto*self.ancho;

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}';

class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,base,altura,color):
        FiguraGeometrica.__init__(self,base,altura);
        Color.__init__(self,color);

    def area(self):
        return self.alto * self.ancho;

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}';

#objetos
print("Objeto Cuadrado".center(50,"-"));
lado = float(input("ingresa el lado: "));
color = input("Ingresa El color: ");


cuadrado1 = Cuadrado(lado,color);
print(f'Calculo area cuadrado: {cuadrado1.CalcularArea()}');
print(cuadrado1.__str__());
print("rectangulo".center(50,"-"));
base = float(input("ingresa la base: "));
altura = float(input("ingresa la altura: "));
color = input("Ingresa El color: ");

rectangulo1 = Rectangulo(base,altura,color);
print(f'Calculo area rectangulo: {rectangulo1.area()}');
print(rectangulo1.__str__());