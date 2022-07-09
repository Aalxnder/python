class Clase:
    #variable de clase
    variableDeClase = "valor de clase";

    def __init__(self,variableDeInstancia):
        ##variable de instancia
        self.variableDeInstancia = variableDeInstancia;

    #metodos estaticos (no puede acceder ni a los objetos(self) ni sus instancias)

    @staticmethod
    def metodoEstatico():
        print(Clase.variableDeClase);

#llamar al metodo estatico
Clase.metodoEstatico();