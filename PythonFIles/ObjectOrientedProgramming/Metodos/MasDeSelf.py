#se puede poner this sin problemas en ves de self
class Persona:
    def __init__(this,nombre,apellido,edad):
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;

    def mostrarDetalle(this):
        print(f'Persona: {this.nombre} {this.apellido} tiene {this.edad} años ',end="");

persona1 = Persona("Levi","Perez",18);
persona1.mostrarDetalle();

##Se pueden agregar nuevos argumentos a los objetos, pero solo sera para ese objeto en especifico
persona1.telefono = '3322895914';
print(f'numero de telefono: {persona1.telefono}');

print("");

persona2 = Persona("Valeria","Gonzales",18)
persona2.mostrarDetalle();
