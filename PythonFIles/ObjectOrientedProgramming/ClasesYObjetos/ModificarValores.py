#Creacion de objetos con argumentos

class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = edad;
Persona1 = Persona("levi","perez",18);
Persona2 = Persona("Valeria","Gonzales",18);

Persona1.nombre = "Alexander";

print(f'{Persona1.nombre} {Persona1.apellido}: {Persona1.edad}');
print(f'{Persona2.nombre} {Persona2.apellido}: {Persona2.edad}');