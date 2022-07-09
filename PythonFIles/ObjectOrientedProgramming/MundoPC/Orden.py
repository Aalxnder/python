from Computadora import Computadora;
from Raton import Raton;
from Teclado import Teclado;
from Monitor import Monitor;
class Orden:
    contador = 0;
    #metodo de clase
    @classmethod
    def contadorOrdenes(cls):
        cls.contador += 1;
        return cls.contador;

    #metodo Init
    def __init__(self,computadora):
        self.idComputadora = Orden.contadorOrdenes();
        self._Ordenes = list(computadora);

    def agregarCompu(self,computadora):
        self.Ordenes.append(computadora);

    def __str__(self):
        compus_str = "";
        for compu in self._Ordenes:
            compus_str += compu.__str__()+"";
        return "ID Orden "+str(self.idComputadora)+":\n\t"+compus_str+"\n";

if __name__ == '__main__':
    raton = Raton("USB","hyper x");
    teclado = Teclado("USB","Logitech");
    monitor = Monitor("LG","LG-U24M40","24 pulgadas");
    computadora = Computadora("HP",raton,teclado,monitor);
    computadora2 = Computadora("HP",raton,teclado,monitor);
    listaComputadoras = [computadora,computadora2];
    listaComputadoras2 = [computadora];
    orden = Orden(listaComputadoras);
    orden2 = Orden(listaComputadoras2);

    print(orden.__str__());
    print(orden2.__str__())