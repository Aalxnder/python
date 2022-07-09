from Ticket import Producto
from Orden import Orden
producto1 = Producto('camisa', 200);
producto2 = Producto('pantalon', 300);
producto3 = Producto('zapatos', 400);
producto4 = Producto('sombrero', 500);

productos = [producto1, producto2];

productos2 = [producto1, producto2, producto3, producto4];

Orden1 = Orden(productos);
Orden1.agregar(producto3);
print(Orden1.__str__());
Orden2 = Orden(productos2);
print(Orden2.__str__());