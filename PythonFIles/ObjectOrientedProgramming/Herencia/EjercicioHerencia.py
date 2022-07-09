# definir una clase padre llamada vehiculo y dos clases hijas llamadas coche y bicicleta,
# las cuales heredan de la clase padre
# La clase padre debe tener los siguientes atributos
#
# vehiculo(clase padre):
# -atributos(color, ruedas)
# -metodos(__init__() y __str()__)
#
# coche clase hija ademas de los metodos heredados debe tener el atributo
# -atributos(velocidad)
# -metodos(__init__() 7 __str__())
#
# Bicicleta clase hija ademas de los metodos heredados debe tener
# -atributos(tipo(urbana/montaña,etc))
# -metodos(__init__() y __str__())

#clase padre
class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color;
        self.ruedas = ruedas;

    def __str__(self):
        return f'Vehiculo:\nColor: {self.color}\nRuedas: {self.ruedas}';

#clase Hija Vehiculos
class Coche(Vehiculo):
    def __init__(self,color,ruedas,Velocidad):
        super().__init__(color,ruedas);
        self.Velocidad = Velocidad;

    def __str__(self):
        return f'{super().__str__()}\nvelocidad {self.Velocidad}km/h';

#clase hija bicis
class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas);
        self.tipo = tipo;
    def __str__(self):
        return f'{super().__str__()}\ntipo: {self.tipo}';

#objetos
color = input("Ingresa el color del vehiculo: ");
ruedas = input("Ingresa las ruedas del vehiculo: ");

vehiculo1 = Vehiculo(color,ruedas);
print(vehiculo1.__str__());
print("\n\n");

velocidad = float(input("Ingresa la velocidad a la que va el coche: "));
coche = Coche(color,ruedas,velocidad);
print(coche.__str__());
print("\n\n");


tipo = input("ingresa el tipo de la bicicleta: ");
ruedas = 2;
bici = Bicicleta(color,ruedas, tipo);
print(bici.__str__());
print("\n\n");

