from DispositivoEntrada import DispositivoEntrada
from Raton import Raton;
class Teclado(DispositivoEntrada):
    contador = 0;
    #metodo de clase
    @classmethod
    def contadorTeclado(cls):
        cls.contador += 1;
        return cls.contador;

    #metodo Init
    def __init__(self,tipoEntrada,marca):
        super().__init__(tipoEntrada,marca);
        self.idTeclado = Teclado.contadorTeclado();

    #metodo str
    def __str__(self):
        return "ID Teclado "+str(self.idTeclado)+": Tipo de entrada: "+self.tipoEntrada+" Marca: "+self.marca;

if(__name__ == '__main__'):
    teclado = Teclado("USB","Logitech");
    print(teclado.__str__());
    teclado2 = Teclado("USB","Five Magics");
    print(teclado2.__str__());
    raton = Raton("USB","hyper x");
    print(raton.__str__());