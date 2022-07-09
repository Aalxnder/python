#poner dos guiones bajos hace que no podamos modificar el acceso a un atributo fuera de la clase
#poner un guion bajo indica que no deberias poder modificar un argumento pero aun asi se puede

class Persona:
    ##pasar una tupla o diccionario(primero se pasan las tuplas y despues los diccionarios
    def __init__(self,nombre,apellido,edad):
        self.__nombre = nombre;
        self._apellido = apellido;
        self._edad = edad;

    def mostrarDetalle(self):
        print(f'Persona: {self.__nombre} {self._apellido} tiene {self._edad} años');

persona1 = Persona("Levi","Perez",18);
persona1.__nombre = "Levi Alexander";
persona1.mostrarDetalle();

persona2 = Persona("Valeria","Gonzales",18);
persona2.mostrarDetalle();
