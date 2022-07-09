##contador de objetos

class Persona:
    contadorPersonas = 0;

    @classmethod
    def _GenerarSigValor(cls):
        cls.contadorPersonas += 1;
        return cls.contadorPersonas;

    def __init__(self,nombre,edad):
        self.idPersona = Persona._GenerarSigValor();
        self.nombre = nombre;
        self.edad = edad;


    def __str__(self):
        return f'{self.nombre} tiene {self.edad} Persona numero {self.idPersona}';

persona = Persona('Juan',20);
print(persona.__str__());

persona2 = Persona('Pedro',30);
print(persona2.__str__())

persona3 = Persona('Maria',40);
print(persona3.__str__());

Persona4 = Persona('mayra',18);
print(Persona4.__str__());
print("");
print(f'Objetos totales: {Persona.contadorPersonas}');