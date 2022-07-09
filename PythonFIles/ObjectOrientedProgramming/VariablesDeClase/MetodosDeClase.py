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

Clase.metodoStatico();
Clase.metodoDeClase();