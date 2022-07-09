from Ticket import Producto

class Orden:
    #variable de clase, orden
    contador = 0;
    @classmethod
    def _contadorOrdenes(cls):
        cls.contador += 1;
        return cls.contador;


    def __init__(self, productos):
        self._idOrden = Orden._contadorOrdenes();
        self._productos = list(productos);

    ##funcion de agregar
    def agregar(self,producto):
        #agregar un producto a la lista de productos
        self._productos.append(producto);

    def calcularTotal(self):
        total = 0;
        for producto in self._productos:
            total += producto.precio #aplicar el metodo getPrecio;
        return total;


    def __str__(self):
        productos_str = '';
        for producto in self._productos:
            productos_str += producto.__str__()+'\n';
        return f'Orden numero {self._idOrden}:\n{productos_str}Total: {self.calcularTotal()}\n\n';

if (__name__ == '__main__'):
    producto1 = Producto('camisa', 200);

    producto2 = Producto('pantalon', 300);

    productos = [producto1, producto2];
    Orden1 = Orden(productos);
    print(Orden1.__str__());
    Orden2 = Orden(productos);
    print(Orden2.__str__());