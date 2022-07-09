#lo mismo que con las figuras de herencia multiple pero con metodos abstractos
#tenemos que heredar de ABC para convertir la clase en una clase abstracta

from abc import ABC,abstractmethod;

#Nota: no se pueden instanciar las clases abstractas

class FiguraGeometrica(ABC):
    def __init__(self,alto,ancho):
        if(self._validarValor(ancho)):
            self._alto = alto;
        else:
            print(f'{alto} es un dato Invalido');
            self._alto = 0;
        if(self._validarValor(alto)):
            self._ancho = ancho;
        else:
            print(f'{ancho} es un dato Invalido');
            self._ancho = 0;
    #setters y getter
    @property
    def alto(self):
        return self._alto;
    #Quitar setters si no queremos q los datos se modifiquen despues
    @alto.setter
    def alto(self,alto):
        if(self._validarValor(alto)):
            self._alto = alto;
        else:
            print(f'{alto} es un dato Invalido');
            self._alto = 0;

    @property
    def ancho(self):
        return self._ancho;

    @ancho.setter
    def ancho(self, ancho):
        if(self._validarValor(ancho)):
            self._ancho = ancho;
        else:
            print(f'{ancho} es un dato Invalido');
            self._ancho = 0;
    #Metodo Abstracto
    @abstractmethod
    def area(self):
        pass;

    def __str__(self):
        return f'Datos de la figura:\nAlto: {self._alto},Ancho: {self._ancho}';

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
    def area(self):
        return self.ancho*self.alto;
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}';

class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,base,altura,color):
        FiguraGeometrica.__init__(self,base,altura);
        Color.__init__(self,color);
    def area(self):
        return self.ancho *self.alto;
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}';

print("Objeto cuadrado".center(50,"-"));
lado = float(input("ingresa el lado: "));
color = input("ingresa el color de la figura: ");
cuadrado = Cuadrado(lado,color);
print("El area del cuadrado es: ",cuadrado.area());
print(cuadrado.__str__());

print("Objeto Rectangulo".center(50,"-"));
base = float(input("ingresa la base del rectangulo: "));
altura = float(input("Ingresa la altura del rectangulo: "));
color = input("ingresa el color de la figura: ");
rectangulo = Rectangulo(base,altura,color);
print("EL area es: ",rectangulo.area());
print(rectangulo.__str__());
