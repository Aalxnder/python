# los objetos con contexto dinamico si puede acceder a los metodos estaticos de la clase
# pero un objeto estatico no puede acceder a los metodos dinamicos de la clase

class Clase:
    #variable de clase
    variableDeClase = "valor de clase";

    def __init__(self,variableDeInstancia):
        ##variable de instancia
        self.variableDeInstancia = variableDeInstancia;

    #metodo estatico
    @staticmethod
    def metodoStatico():
        print(Clase.variableDeClase);

    #metodos de clase
    @classmethod
    def metodoDeClase(cls):
        print(cls.variableDeClase);

    def metodoDeInstancia(self):
        self.metodoDeClase();
        self.metodoStatico();


Clase.metodoStatico();
Clase.metodoDeClase();
objeto = Clase('Valor de instancia');
objeto.metodoDeClase();
objeto.metodoDeInstancia();