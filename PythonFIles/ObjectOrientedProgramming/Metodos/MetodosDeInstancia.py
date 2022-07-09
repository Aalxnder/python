class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = edad;

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} tiene {self.edad} años');

persona1 = Persona("Levi","Perez",18);
persona1.mostrarDetalle();

persona2 = Persona("Valeria","Gonzales",18)
persona2.mostrarDetalle();
