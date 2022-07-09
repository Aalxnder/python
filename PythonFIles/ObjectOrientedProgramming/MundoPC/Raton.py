#clase orden
#crear una clase llamada orden que tendra un contador de objetos del tipo orden y un atributo privado llamado ID orden
#tambien la variablecontador ordenes de tipo static es la encargada de generar un id unico por cada objeto, es decir incrementarla en uno
# cada que creemos un objeto y su valor se lo asiganeremos a la variable IDorden asi mismo una variable de tipo lista privada llamada computadora
#y lo mismo con las clases computadoras ,monitor,raton,teclado obviamente cada una con sus respectiuvos contadores
#tendra un atributo llamado computadoras recibido desde el metodo init y podemos agregar una nueva computadora desde el metodo
# agregar computadora para agregar un elemento extra a demas de crear el metodo str para la clase, una orden puede tener 1 o muchas computadoras
#la responsabilidad de esta clase es crear objetos del tipo orden que almacene en una lista los objetos del tipo computadora

#clase computadora;
#tener una variable estatica llamada contador computadoras, y asignarle el valor a la variable IDComputadoras
#inicializaremos el metodo init con los atributos
# nombre - String
# monitor - Monitor
# teclado - Teclado;
# raton - raton;
# asi mismo imprimir la clase str
#y los metodos set y get de cada atributo

#clase Monitor
# se comporta igual el contador a las demas clases,
#debemos agregar los atributos marca,tamaño de tipo String
#y los metodos set y get de cada atributo junto a la clase str
#aqui se crean los objetos del tipo monitor

#dispositivo entrada
#esta clase es clase padre de la clase raton y teclado tiene que tener los atributos
# tipo entrada y marca, sin necesidad de usar los metodos set y get

# clase Raton
# esta clase hereda de dispositivo de entrada, igual tiene un contador, un atributo privado llamado IDRaton
#agregar el metodo str con los atributos protegidos de la clase padre

# clase Teclado
# lo mismo que la clase raton

# y al final una clase prueba
from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador = 0;
    @classmethod
    def _getContador(cls):
        cls.contador += 1;
        return cls.contador
    def __init__(self, marca,tipoEntrada):
        super().__init__(marca,tipoEntrada);
        self.idRaton = Raton._getContador();
    def __str__(self):
        return "Raton: " +str(self.idRaton)+" Tipo de entrada: "+self.tipoEntrada+" Marca: "+self.marca;
#
if(__name__ == '__main__'):
    raton = Raton("Logitech","USB");
    print(raton.__str__());
    raton2 = Raton("fiveMagics","USB");
    print(raton2.__str__());