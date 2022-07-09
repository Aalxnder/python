from Raton import Raton;
from Teclado import Teclado;
from Monitor import Monitor;
class Computadora(object):
    contador = 0;
    #variable de clase
    @classmethod
    def contadorComputadora(cls):
        cls.contador += 1;
        return cls.contador;
    def __init__(self, nombre,monitor,teclado,raton):
        self._nombre = nombre;
        self._monitor = monitor;
        self._teclado = teclado;
        self._raton = raton;
        self.idComputadoras = Computadora.contadorComputadora();

    #setters y getters
    @property
    def nombre(self):
        return self._nombre;
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;
    @property
    def monitor(self):
        return self._monitor;
    @monitor.setter
    def monitor(self,monitor):
        self._monitor = monitor;
    @property
    def teclado(self):
        return self._teclado;
    @teclado.setter
    def teclado(self,teclado):
        self._teclado = teclado;
    @property
    def raton(self):
        return self._raton;
    @raton.setter
    def raton(self,raton):
        self._raton = raton;

    #metodo str
    def __str__(self):
        return "ID Computadora "+str(self.idComputadoras)+": Nombre: "+str(self.nombre)+"\n\t"+str(self.monitor)+"\n\t"+str(self.teclado)+"\n\t"+str(self.raton)+"\n\n";

#objetos
if(__name__ == '__main__'):
    raton = Raton("USB","hyper x");
    teclado = Teclado("USB","Logitech");
    monitor = Monitor("LG","LG-U24M40","24 pulgadas");
    computadora = Computadora("HP",raton,teclado,monitor);
    print(computadora.__str__());