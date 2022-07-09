#variables de clase, son las variables que se definen en la clase
# y no en los metodos

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

clase2 = Clase('Valor de instancia 2');
print(clase2.variableDeClase);
print(clase2.variableDeInstancia);