#realizar dos clases una para el ticket y otra para los productos
#la clase de orden debe tener un contador de ordenes, un id de orden y una lista de los productos
#ademas del metodo __str__()
#la clase producto debe tener un metodo de clase llamado contador de productos
#y las variables id de producto, nombre, y precio ademas del metodo __str__()

import random;
class Producto:
    idProducto = 0;
    @classmethod
    def contadorProductos(cls):
        cls.idProducto = random.randint(1,100);
        return cls.idProducto;

    def __init__(self,nombre,precio):
        self._codigoProducto = Producto.contadorProductos();
        self._nombre = nombre;
        self._precio = precio;

    @property
    def nombre(self):
        return self._nombre;
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;

    @property
    def precio(self):
        return self._precio;
    @precio.setter
    def precio(self,precio):
        self._precio = precio;

    @property
    def codigoProducto(self):
        return self._codigoProducto;
    @codigoProducto.setter
    def codigoProducto(self,codigoProducto):
        self._codigoProducto = codigoProducto;

    def __str__(self):
        return f'ID Producto {self._codigoProducto}:\nNombre: {self._nombre}\nPrecio: {self._precio}\n\n';

class Orden(Producto):
    contadorOrdenes = 0;




#objetos
if(__name__ == '__main__'):
    producto1 = Producto('camisa',200);
    print(producto1.__str__());
    producto2 = Producto('pantalon',300);
    print(producto2.__str__());
