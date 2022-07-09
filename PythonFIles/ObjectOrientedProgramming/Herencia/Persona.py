#definir clase padre
class Persona:
    def __init__(self,nombre,edad):

        self.nombre = nombre;
        self.edad = edad;

    #metodo str
    def __str__(self):
        return f'Persona: Nombre {self.nombre}, edad: {self.edad}'


#definir clase Hija
class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad);
        self.sueldo = sueldo;
    # def mostrarDatos(self):
    #     print(f'Nombre {self.nombre}, edad: {self.edad}, sueldo: {self.sueldo}');

    def __str__(self):
        return (f'Empleado: {super().__str__()} sueldo: {self.sueldo}');


#objetos
# if __name__ == '__main--':
#     empleado1 = Empleado('levi',18,5000);
#     empleado1.mostrarDatos();