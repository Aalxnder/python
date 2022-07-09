class Persona:
    def __init__(self,nombre ,edad):
        self.nombre = nombre;
        self.edad = edad;

    #sobre escribir el metodo suma
    def __add__(self,other):
        return self.nombre + other.nombre;

    #sobre escribir el metodo resta
    def __sub__(self, other):
        return self.edad - other.edad;

obj1 = Persona("Juan ",28);
obj2 = Persona("Pedro",20);
print(obj1 + obj2);
print(obj1 - obj2);
# obj1.__add__(obj2)
