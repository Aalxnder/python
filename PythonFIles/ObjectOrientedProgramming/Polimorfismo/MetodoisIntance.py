from PoliEmpleado import *;

def imprimirDetalles(objeto):
    print(objeto);
    print(type(objeto));
    #revisar si el objeto recibido es de cierta instancia
    if isinstance(objeto,Gerente):
        print(objeto.departamento);

empleado = Empleado("Juan",30,1000);
imprimirDetalles(empleado);

gerente = Gerente("Juan",30,1000,"RRHH");
imprimirDetalles(gerente);

