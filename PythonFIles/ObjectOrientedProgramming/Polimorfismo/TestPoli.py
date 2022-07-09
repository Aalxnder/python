from PoliEmpleado import *;

def imprimirDetalles(objeto):
    print(objeto);
    print(type(objeto));

empleado = Empleado("Juan",30,1000);
imprimirDetalles(empleado);

gerente = Gerente("Juan",30,1000,"RRHH");
imprimirDetalles(gerente);

