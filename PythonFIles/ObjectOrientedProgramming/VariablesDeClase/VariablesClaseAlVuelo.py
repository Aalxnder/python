class Clase:
    #variable de clase
    variableDeClase = "valor de clase";

    def __init__(self,variableDeInstancia):
        ##variable de instancia
        self.variableDeInstancia = variableDeInstancia;

print(Clase.variableDeClase);
persona = Clase('Valor de instancia');
print(persona.variableDeInstancia);
print(persona.variableDeClase);

Clase.variableDeClase = "Nuevo valor de clase"; #cambiar el dato de la variable de claser

clase2 = Clase('Valor de instancia 2');
print(clase2.variableDeClase);
print(clase2.variableDeInstancia);