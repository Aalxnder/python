class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre;
        self.edad = edad;

    def esMayorDeEdad(self,func):
        return func(18);

def mayorUsa(edad):
    if(edad >= 21):
        return True;
    else:
        return False;

def mayorMex(edad):
    if(edad >= 10):
        return True;
    else:
        return False;

nombre = input("ingresa el nombre de la persona: ")
edad = int(input(f"ingresa la edad de {nombre}: "));

persona = Persona(nombre,edad);
if(persona.esMayorDeEdad(mayorUsa)):
    print(f"La persona {persona.nombre} es mayor de edad en estados unidos, tiene {persona.edad} años");
else:
    print("La persona no es mayor de edad en estados unidos");

if(persona.esMayorDeEdad(mayorMex)):
    print("La persona es mayor de edad en mexico");
else:
    print("La persona no es mayor de edad en mexico");