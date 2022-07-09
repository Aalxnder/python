class Persona:
    ##equivalente al constructor
    def __init__(self):
        self.nombre = 'Juan';
        self.apellido = 'Gonzales';
        self.edad = 29;


##creacion del objeto
Persona1 = Persona();
print(f' nombre: {Persona1.nombre} {Persona1.apellido} edad: {Persona1.edad}');


