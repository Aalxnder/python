from Raton import Raton;
from Teclado import Teclado;

class Monitor(object):
    contador = 0;
    @classmethod
    def contadorMonitor(cls):
        cls.contador += 1;
        return cls.contador;
    def __init__(self,marca,modelo,tamanio):
        self._marca = marca;
        self._modelo = modelo;
        self._tamanio = tamanio;
        self.idMonitor = Monitor.contadorMonitor();

    #setters y getters
    @property
    def marca(self):
        return self._marca;
    @marca.setter
    def marca(self,marca):
        self._marca = marca;
    @property
    def modelo(self):
        return self._modelo;
    @modelo.setter
    def modelo(self,modelo):
        self._modelo = modelo;
    @property
    def tamanio(self):
        return self._tamanio;
    @tamanio.setter
    def tamanio(self,tamanio):
        self._tamanio = tamanio;

    def __str__(self):
        return "ID Monitor "+str(self.idMonitor)+": Marca: "+self.marca+" Modelo: "+self.modelo+" Tamaño: "+self.tamanio;

#objetos
if(__name__ == '__main__'):
    monitor1 = Monitor("LG","LG-U24M40","24 pulgadas");
    print(monitor1.__str__());
    monitor2 = Monitor("Samsung","SAMSUNG-U24M40","24 pulgadas");
    print(monitor2.__str__());
    raton = Raton("USB","hyper x");
    print(raton.__str__());
    teclado = Teclado("USB","Logitech");
    print(teclado.__str__());