class Persona:
    ##pasar una tupla o diccionario(primero se pasan las tuplas y despues los diccionarios
    def __init__(self,nombre,apellido,edad,*tuplas,**diccionario):
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = edad;
        self.tuplas = tuplas;
        self.diccionario = diccionario;

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} tiene {self.edad} años {self.tuplas} {self.diccionario}');

persona1 = Persona("Levi","Perez",18,"3322895914",2,3,5,u='Uvas',f='fresa');
persona1.mostrarDetalle();

persona2 = Persona("Valeria","Gonzales",18,m='Manzana',p='Pera');
persona2.mostrarDetalle();
